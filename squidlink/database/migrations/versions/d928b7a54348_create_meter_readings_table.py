"""create meter readings table

Revision ID: d928b7a54348
Revises: 25162b263575
Create Date: 2024-07-01 17:20:24.002356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd928b7a54348'
down_revision: Union[str, None] = '25162b263575'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'meter_readings',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('facility_id', sa.Integer, sa.ForeignKey('facilities.id', ondelete='CASCADE'), nullable=False),
        sa.Column('type', sa.Enum('Electricity', 'Gas', name='meterreadingtype'), nullable=False),
        sa.Column('consumption', sa.Float, nullable=False),
        sa.Column('unit', sa.Enum('kWh', name='meterreadingunit'), nullable=False),
        sa.Column('interval_start', sa.DateTime, nullable=False),
        sa.Column('interval_end', sa.DateTime, nullable=False)
    )

def downgrade():
    op.drop_table('meter_readings')
