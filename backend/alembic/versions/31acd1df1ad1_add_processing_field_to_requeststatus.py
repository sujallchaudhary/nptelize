"""add processing field to RequestStatus

Revision ID: 31acd1df1ad1
Revises: 988cb0fc5478
Create Date: 2025-05-18 21:32:30.041527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31acd1df1ad1'
down_revision: Union[str, None] = '988cb0fc5478'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TYPE requeststatus ADD VALUE 'processing' AFTER 'pending'")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
