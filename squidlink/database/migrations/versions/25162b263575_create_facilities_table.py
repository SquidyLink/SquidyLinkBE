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


def upgrade():
    op.create_table(
        'facilities',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('address_line_1', sa.String, nullable=True),
        sa.Column('address_line_2', sa.String, nullable=True),
        sa.Column('address_postcode', sa.String, nullable=True),
        sa.Column('address_city', sa.String, nullable=True),
        sa.Column('address_country', sa.String, nullable=True),
        sa.Column('bms', sa.String, nullable=True),
        sa.Column('sector', sa.Enum('Agriculture', 'Commercial', 'Industrial', 'Residential', 'Other', name='facilitysector'), nullable=False),
        sa.Column('floor_area_square_metres', sa.Integer, nullable=True),
    )

def downgrade():
    op.drop_table('facilities')
