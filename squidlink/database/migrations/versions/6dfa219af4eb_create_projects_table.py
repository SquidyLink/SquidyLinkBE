"""create projects table

Revision ID: 6dfa219af4eb
Revises: b9bc9f72ad42
Create Date: 2024-07-01 17:37:50.445654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6dfa219af4eb'
down_revision: Union[str, None] = 'b9bc9f72ad42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('facility_id', sa.Integer, sa.ForeignKey('facilities.id', ondelete='CASCADE'), nullable=False),
    )


def downgrade() -> None:
    pass
