"""Create accounts table.

Revision ID: 20251230_01
Revises:
Create Date: 2025-12-30 16:42:23.375564
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20251230_01"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Apply the migration."""
    op.create_table(
        "accounts",
        sa.Column(
            "id",
            sa.UUID(),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.UniqueConstraint("email", name="uq_accounts_email"),
    )


def downgrade() -> None:
    """Revert the migration."""
    op.drop_table("accounts")
