"""Populate stats table.

Revision ID: c9334d3bae92
Revises: 63dd8a1ce0df
Create Date: 2020-12-06 19:12:00.336071

"""
from alembic import op
import sqlalchemy as sa

from src.model.user import User
from src.model.stat import Stat


# revision identifiers, used by Alembic.
revision = 'c9334d3bae92'
down_revision = '63dd8a1ce0df'
branch_labels = None
depends_on = None


def upgrade():
    for user in User.query.all():
        op.execute(
            sa.insert(Stat).
            values(user_id=user.id)
        )


def downgrade():
    op.execute(
        sa.delete(Stat)
    )
