"""Create outbox table.

Revision ID: 20251230_02
Revises: 20251230_01
Create Date: 2025-12-30 16:42:27.531386
"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "20251230_02"
down_revision: str | None = "20251230_01"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Apply the migration."""
    op.create_table(
        "outbox",
        sa.Column(
            "id",
            sa.UUID(),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column("aggregate_type", sa.String(length=255), nullable=False),
        sa.Column("aggregate_id", sa.String(length=255), nullable=False),
        sa.Column(
            "payload",
            postgresql.JSONB(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "processed_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
        sa.Index(
            "ix_outbox_unprocessed",
            "processed_at",
        ),
    )


def downgrade() -> None:
    """Revert the migration."""
    op.drop_table("outbox")
