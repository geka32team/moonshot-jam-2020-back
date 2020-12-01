"""Populate stats table.

Revision ID: b65791a62e04
Revises: e631352c5582
Create Date: 2020-11-29 18:22:23.327735

"""
from alembic import op
import sqlalchemy as sa

from src.model.user import User
from src.model.stat import Stat


# revision identifiers, used by Alembic.
revision = 'b65791a62e04'
down_revision = 'e631352c5582'
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
