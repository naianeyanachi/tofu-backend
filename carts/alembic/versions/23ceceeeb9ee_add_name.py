"""add_name

Revision ID: 23ceceeeb9ee
Revises: dd33cb03d01f
Create Date: 2021-12-05 15:44:02.250851

"""

# revision identifiers, used by Alembic.
revision = '23ceceeeb9ee'
down_revision = 'dd33cb03d01f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('carts',
        sa.Column('name', sa.String())
    )


def downgrade():
    op.drop_column('carts', 'name')
