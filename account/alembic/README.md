# Alembic

This directory contains database migration scripts managed by Alembic.

Execute the following commands in the `account` directory.

## Sync migration dependencies

First, sync your local environment with the migration dependencies:

```bash
uv sync --group migration
```

## Create a new revision

To create a blank revision script:

```bash
uv run alembic revision -m "describe your change"
```

## Apply migrations (Upgrade)

To upgrade to the latest version:

```bash
uv run alembic upgrade head
```

To upgrade to a specific version:

```bash
uv run alembic upgrade <revision_id>
```

## Revert migrations (Downgrade)

To downgrade to the very first version (empty database):

```bash
uv run alembic downgrade base
```

To downgrade to a specific version:

```bash
uv run alembic downgrade <revision_id>
```

## View migration status

To see the current revision:

```bash
uv run alembic current
```

To view the history of revisions:

```bash
uv run alembic history
```
