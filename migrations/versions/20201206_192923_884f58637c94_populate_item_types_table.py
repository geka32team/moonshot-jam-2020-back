"""Populate item_types table.

Revision ID: 884f58637c94
Revises: c7945a1a032b
Create Date: 2020-12-06 19:29:23.969046

"""
from alembic import op
import sqlalchemy as sa

from src.model.item_type import ItemType


# revision identifiers, used by Alembic.
revision = '884f58637c94'
down_revision = 'c7945a1a032b'
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
