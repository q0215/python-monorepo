# Account Module

[![uv](https://img.shields.io/badge/managed%20with-uv-blue.svg)](https://github.com/astral-sh/uv)

This module provides the core functionality for managing user accounts within the
system. It defines the data models, business logic, and APIs related to user accounts.

## Purpose

-   Define and manage user account data models
-   Provide APIs for account creation, modification, and retrieval

## Principles

-   **Domain-Specific Logic**: This module encapsulates the business logic specific to
    user accounts.
-   **Well-Defined APIs**: Expose clear and consistent APIs for other modules to
    interact with user accounts.
-   **Security First**: Prioritize security best practices in all aspects of account
    management and data protection.

## Usage

This module provides the necessary tools to manage user accounts within the system.

```python
# Example: Creating a new account
from account.service import AccountService

account_service = AccountService()
account = account_service.create_account(username="newuser", email="newuser@example.com")
print(f"Created account with ID: {account.account_id}")
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
