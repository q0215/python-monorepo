"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""

from collections.abc import Sequence

revision: str = "${up_revision}"
down_revision: str | None = ${repr(down_revision)}
branch_labels: str | Sequence[str] | None = ${repr(branch_labels)}
depends_on: str | Sequence[str] | None = ${repr(depends_on)}


def upgrade() -> None:
    """Apply the migration."""
% if upgrades:
${upgrades}
% else:
    msg = "Upgrade logic is not implemented"
    raise NotImplementedError(msg)
% endif


def downgrade() -> None:
    """Revert the migration."""
% if downgrades:
${downgrades}
% else:
    msg = "Downgrade logic is not implemented"
    raise NotImplementedError(msg)
% endif
