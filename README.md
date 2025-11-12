# Python Monorepo

Welcome to the `python-monorepo` monorepo! This repository contains multiple independent
Python projects, each managed within its own directory.

## Guiding Principles

This monorepo follows a few key principles to maintain project independence and clarity:

-   **Project Isolation**: Each project folder is self-contained and independent. It
    manages its own dependencies and logic.
-   **Cross-Project Dependencies**: When one project needs to depend on another from
    this monorepo (e.g., `account` using `shared`), it does so by consuming a versioned
    wheel file. These wheel files are expected to be generated and published from Git
    releases. This practice avoids direct path-based imports between projects, ensuring
    they are decoupled.
-   **Tooling Flexibility**: While projects are independent, the repository encourages
    streamlined development. For example, `uv` is a fast package manager that works well
    in this setup, but each project is free to choose its own tools like Poetry or PDM.

## Projects

The following projects currently reside in this monorepo:

| Project    | Description                                                                            |
| ---------- | -------------------------------------------------------------------------------------- |
| `shared/`  | A library of shared, domain-agnostic models and utilities for use across all projects. |
| `account/` | The account domain, responsible for managing user accounts.                            |

## Development Environment

Please refer to the `README.md` file inside each project's directory for specific setup
and usage instructions.

## Build and Publishing

When a project (e.g., `shared`) is updated, a new version of its wheel file should be
built and published. This monorepo is designed to automate this process through a CI/CD
pipeline (e.g., using GitHub Actions) triggered on new Git releases.

Developers consuming these packages should update their `pyproject.toml` to point to the
new version.
