"""create a bids table

Revision ID: b9bc9f72ad42
Revises: 3cf5000a00f0
Create Date: 2024-07-01 17:18:37.622149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9bc9f72ad42'
down_revision: Union[str, None] = '3cf5000a00f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('bids',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('duration', sa.Integer(), nullable=True),
        sa.Column('site_inspection', sa.Boolean(), nullable=True),
        sa.Column('estimated_savings', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('bids')
