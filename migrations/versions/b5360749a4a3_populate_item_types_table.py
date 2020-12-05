"""Populate item_types table.

Revision ID: b5360749a4a3
Revises: 0c5a24ddc71b
Create Date: 2020-12-05 19:28:14.665266

"""
from alembic import op
import sqlalchemy as sa

from src.model.item_type import ItemType


# revision identifiers, used by Alembic.
revision = 'b5360749a4a3'
down_revision = '0c5a24ddc71b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        sa.insert(ItemType).values([
            {'name': 'Weapon', 'slug': 'weapon'},
            {'name': 'Helm', 'slug': 'helm'},
            {'name': 'Armor', 'slug': 'armor'},
            {'name': 'Gloves', 'slug': 'gloves'},
            {'name': 'Boots', 'slug': 'boots'},
            ])
    )


def downgrade():
    op.execute(
        sa.delete(ItemType)
    )
