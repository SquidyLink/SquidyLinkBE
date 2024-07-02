"""create a contractors table

Revision ID: 3cf5000a00f0
Revises: 25162b263575
Create Date: 2024-07-01 17:02:14.314593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cf5000a00f0'
down_revision: Union[str, None] = '6dfa219af4eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'contractors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address_line_1', sa.String(), nullable=True),
        sa.Column('address_line_2', sa.String(), nullable=True),
        sa.Column('address_postcode', sa.String(), nullable=True),
        sa.Column('address_city', sa.String(), nullable=True),
        sa.Column('address_country', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'skills',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'contractors_skills',
        sa.Column('contractor_id', sa.Integer(), nullable=False),
        sa.Column('skill_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['contractor_id'], ['contractors.id'], ),
        sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
        sa.PrimaryKeyConstraint('contractor_id', 'skill_id')
    )

    op.create_table(
        'projects_skills',
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column('skill_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
        sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
        sa.PrimaryKeyConstraint('project_id', 'skill_id')
    )


def downgrade() -> None:
    op.drop_table('contractors_skills')
    op.drop_table('projects_skills')
    op.drop_table('skills')
    op.drop_table('contractors')
