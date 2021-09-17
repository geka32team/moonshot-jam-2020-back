"""Add and populate rariry_type table.

Revision ID: 8fa0a21e761b
Revises: 1d3966b0946a
Create Date: 2020-12-27 11:37:21.882044

"""
from alembic import op
import sqlalchemy as sa

from src.model.rarity_type import RarityType


# revision identifiers, used by Alembic.
revision = '8fa0a21e761b'
down_revision = '1d3966b0946a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rarity_types',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('slug', sa.String(length=100), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name'),
                    sa.UniqueConstraint('slug')
                    )
    op.execute(
        sa.insert(RarityType).values([
            {'name': 'Common', 'slug': 'common'},
            {'name': 'Rare', 'slug': 'rare'},
            {'name': 'Magic', 'slug': 'magic'},
            {'name': 'Epic', 'slug': 'epic'},
            {'name': 'Legendary', 'slug': 'Legendary'},
        ])
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rarity_types')
    # ### end Alembic commands ###
