"""Populate bonuses table.

Revision ID: 16e732774d70
Revises: f81dc620a415
Create Date: 2020-12-05 21:40:07.706255

"""
from alembic import op
import sqlalchemy as sa

from src.model.bonus import Bonus


# revision identifiers, used by Alembic.
revision = '16e732774d70'
down_revision = 'f81dc620a415'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        sa.insert(Bonus).values([
            {'slug': 'generic'},
            ])
    )


def downgrade():
    op.execute(
        sa.delete(Bonus)
    )
