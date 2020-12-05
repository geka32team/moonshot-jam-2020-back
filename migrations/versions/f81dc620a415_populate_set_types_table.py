"""Populate set_types table.

Revision ID: f81dc620a415
Revises: b5360749a4a3
Create Date: 2020-12-05 21:31:54.728605

"""
from alembic import op
import sqlalchemy as sa

from src.model.set_type import SetType


# revision identifiers, used by Alembic.
revision = 'f81dc620a415'
down_revision = 'b5360749a4a3'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        sa.insert(SetType).values([
            {'name': 'Wooden', 'slug': 'wooden'},
            {'name': 'Iron', 'slug': 'iron'},
            {'name': 'Bronze', 'slug': 'bronze'},
            {'name': 'Silver', 'slug': 'silver'},
            {'name': 'Gold', 'slug': 'gold'},
            {'name': 'Serafim', 'slug': 'serafim'},
            ])
    )


def downgrade():
    op.execute(
        sa.delete(SetType)
    )
