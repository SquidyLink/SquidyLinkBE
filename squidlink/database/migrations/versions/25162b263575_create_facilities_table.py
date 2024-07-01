"""create facilities table

Revision ID: 25162b263575
Revises:
Create Date: 2024-07-01 16:08:45.998651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25162b263575'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # TODO implement
    pass


def downgrade() -> None:
    pass
