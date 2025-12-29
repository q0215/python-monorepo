"""Simple ASGI HTTP endpoints for the account package.

This module implements a minimal ASGI application that supports:
- GET /health -> 200 JSON {"status": "ok"}
- POST /accounts -> create an Account from JSON body and return its dict

The implementation avoids external web frameworks so tests can exercise the
ASGI callable directly.
"""

from __future__ import (
    annotations,
)

import json
from typing import Any

from account.domain.account import (
    Account,
)

JSON_HEADERS = [("content-type", "application/json; charset=utf-8")]


def json_bytes(obj: Any) -> bytes:
    return json.dumps(obj, ensure_ascii=False).encode("utf-8")


async def app(scope, receive, send) -> None:
    """A very small ASGI app handling two routes.

    scope: a mapping with keys like 'type', 'method', 'path'
    This app supports only HTTP requests.
    """
    if scope["type"] != "http":
        # not handling other types (lifespan, ws, etc.)
        await send({"type": "http.response.start", "status": 500, "headers": []})
        await send({"type": "http.response.body", "body": b"", "more_body": False})
        return

    method = scope.get("method", "GET").upper()
    path = scope.get("path", "/")

    try:
        if method == "GET" and path == "/health":
            body = json_bytes({"status": "ok"})
            await send(
                {"type": "http.response.start", "status": 200, "headers": JSON_HEADERS},
            )
            await send({"type": "http.response.body", "body": body, "more_body": False})
            return

        if method == "POST" and path == "/accounts":
            # read request body from receive
            body_bytes = b""
            more_body = True
            while more_body:
                event = await receive()
                if event["type"] == "http.request.body":
                    body_bytes += event.get("body", b"")
                    more_body = event.get("more_body", False)

            if not body_bytes:
                raise ValueError("empty body")

            try:
                data = json.loads(body_bytes.decode("utf-8"))
            except Exception as exc:  # pragma: no cover - parsing error
                raise ValueError("invalid json") from exc

            # minimal validation
            for key in ("email", "name", "password_hash"):
                if key not in data:
                    raise ValueError(f"missing field: {key}")

            acc = Account.create(data["email"], data["name"], data["password_hash"])
            body = json_bytes(acc.to_dict())
            await send(
                {"type": "http.response.start", "status": 201, "headers": JSON_HEADERS},
            )
            await send({"type": "http.response.body", "body": body, "more_body": False})
            return

        # not found
        body = json_bytes({"error": "not found"})
        await send(
            {"type": "http.response.start", "status": 404, "headers": JSON_HEADERS},
        )
        await send({"type": "http.response.body", "body": body, "more_body": False})

    except ValueError as exc:
        body = json_bytes({"error": str(exc)})
        await send(
            {"type": "http.response.start", "status": 400, "headers": JSON_HEADERS},
        )
        await send({"type": "http.response.body", "body": body, "more_body": False})
