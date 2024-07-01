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
    op.create_table('projects',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('address_line_1', sa.String(), nullable=True),
        sa.Column('address_line_2', sa.String(), nullable=True),
        sa.Column('address_postcode', sa.String(), nullable=True),
        sa.Column('address_city', sa.String(), nullable=True),
        sa.Column('address_country', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('skills',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('project_skills',
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column('skill_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
        sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
        sa.PrimaryKeyConstraint('project_id', 'skill_id')
    )


def downgrade() -> None:
    op.drop_table('project_skills')
    op.drop_table('skills')
    op.drop_table('projects')
