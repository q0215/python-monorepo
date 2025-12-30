"""Alembic environment configuration."""

import os
from logging.config import fileConfig

from sqlalchemy import create_engine, pool

from alembic import context

# -------------------------------------------------
# Alembic configuration
# -------------------------------------------------
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# -------------------------------------------------
# Manual migrations only (no autogenerate)
# -------------------------------------------------
target_metadata = None


# -------------------------------------------------
# Helpers
# -------------------------------------------------
def required_env(name: str) -> str:
    """Get a required environment variable or fail with a clear error."""
    try:
        return os.environ[name]
    except KeyError as exc:
        msg = f"Environment variable '{name}' is required to run Alembic migrations"
        raise RuntimeError(msg) from exc


def get_db_url() -> str:
    """Build the database URL for Alembic."""
    return "postgresql+psycopg://{user}:{password}@{host}:{port}/{name}".format(
        user=required_env("DB_USER"),
        password=required_env("DB_PASSWORD"),
        host=required_env("DB_HOST"),
        port=os.environ.get("DB_PORT", "5432"),
        name=required_env("DB_NAME"),
    )


# -------------------------------------------------
# Offline migrations
# -------------------------------------------------
def run_migrations_offline() -> None:
    """Run migrations in offline mode (emit SQL without a DB connection)."""
    context.configure(
        url=get_db_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# -------------------------------------------------
# Online migrations
# -------------------------------------------------
def run_migrations_online() -> None:
    """Run migrations in online mode (connect to the database)."""
    connectable = create_engine(
        get_db_url(),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# -------------------------------------------------
# Entrypoint
# -------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
