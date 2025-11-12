# Shared Module

[![uv](https://img.shields.io/badge/managed%20with-uv-blue.svg)](https://github.com/astral-sh/uv)

This module provides shared definitions and abstractions for use across multiple
domains. It contains value objects, identifiers, and common error types to ensure
consistent and type-safe communication between different parts of the system.

## Purpose

-   Define cross-domain value objects (e.g., `AccountId`, `OrderId`)
-   Provide domain-agnostic utilities (e.g., UUID generation, datetime helpers)
-   Enforce consistency and type safety across domains

## Principles

-   **No domain-specific logic**: Shared code must not depend on `account`, `order`, or
    any other specific domain. This ensures the module remains generic and reusable.
-   **Stable abstractions only**: Expose only long-lived, well-defined types or
    interfaces to prevent breaking changes in downstream domains.
-   **Lightweight by design**: Keep the module minimal to avoid tight coupling and
    unnecessary overhead between domains.

## Usage

This module provides foundational types that can be imported and used directly in your
domain-specific logic.

```python
# Example: Using a shared identifier in another module
from shared.model import AccountId

def process_account(account_id: AccountId):
    print(f"Processing account with ID: {account_id}")
```

## Development Setup

This project uses [uv](https://github.com/astral-sh/uv), an extremely fast Python
package installer and resolver, for dependency management. If you haven't installed it
yet, please follow the
[official installation guide](https://github.com/astral-sh/uv#installation).

To create a virtual environment and install all dependencies, run the following command.
It will create a virtual environment in the `.venv` directory (if it doesn't exist) and
sync it with the dependencies specified in `pyproject.toml`.

```shell
# Install all dependencies, including development tools
uv sync --all-extras
```

## Running Tests

To run the test suite, use the following command:

```shell
uv run pytest
```
