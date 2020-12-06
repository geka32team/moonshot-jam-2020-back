"""Populate bonuses table.

Revision ID: c45a6157275a
Revises: 67ade59c85b0
Create Date: 2020-12-06 19:32:39.398807

"""
from alembic import op
import sqlalchemy as sa

from src.model.bonus import Bonus


# revision identifiers, used by Alembic.
revision = 'c45a6157275a'
down_revision = '67ade59c85b0'
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
