# AuthN Module

[![uv](https://img.shields.io/badge/managed%20with-uv-blue.svg)](https://github.com/astral-sh/uv)

This module provides the core functionality for user authentication within the system.
It handles user login, credential verification, and session management.

## Purpose

-   Authenticate users and verify credentials
-   Manage user sessions and authentication tokens
-   Provide APIs for login, logout, and token validation

## Principles

-   **Security First**: Prioritize security best practices, including secure password
    storage and protection against common attacks.
-   **Standard Compliance**: Adhere to standard authentication protocols and practices.
-   **Reliability**: Ensure the authentication service is highly available and
    performant.

## Usage

This module provides the necessary tools to manage user authentication.

```python
# Example: Authenticating a user
from authn.service import AuthService

auth_service = AuthService()
token = auth_service.login(username="user", password="securepassword")
print(f"User logged in, token: {token}")
```

Refer to the module's documentation for detailed usage instructions.

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
