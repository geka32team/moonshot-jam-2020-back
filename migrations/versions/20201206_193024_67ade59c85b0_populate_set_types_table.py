"""Populate set_types table.

Revision ID: 67ade59c85b0
Revises: 884f58637c94
Create Date: 2020-12-06 19:30:24.545131

"""
from alembic import op
import sqlalchemy as sa

from src.model.set_type import SetType


# revision identifiers, used by Alembic.
revision = '67ade59c85b0'
down_revision = '884f58637c94'
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
