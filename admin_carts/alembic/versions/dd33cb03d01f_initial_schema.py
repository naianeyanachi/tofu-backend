'''initial schema

Revision ID: dd33cb03d01f
Revises:
Create Date: 2021-07-23 13:51:31.034548

'''

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'dd33cb03d01f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'carts',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String()),
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'departments',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'sectors',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('department_id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(
            ['department_id'], ['departments.id'],
            name='fk_department_id_sectors'
        ),
    )

    op.create_table(
        'categories',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('sector_id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(
            ['sector_id'], ['sectors.id'],
            name='fk_sector_id_categories'
        ),
    )

    op.create_table(
        'products',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('sku', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('category_id', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(
            ['category_id'], ['categories.id'],
            name='fk_category_id_products'
        ),
    )

    op.create_table(
        'cart_items',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('cart_id', sa.String(), nullable=False),
        sa.Column('product_id', sa.String(), nullable=False),
        sa.Column('quantity', sa.DECIMAL(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(
            ['cart_id'], ['carts.id'],
            name='fk_cart_id_cart_items'
        ),
        sa.ForeignKeyConstraint(
            ['product_id'], ['products.id'],
            name='fk_product_id_cart_items'
        ),
    )

    op.create_table(
        'metadata_fields',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('field', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'metadata_values',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('field_id', sa.String(), nullable=False),
        sa.Column('product_id', sa.String(), nullable=False),
        sa.Column('value', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(
            ['field_id'], ['metadata_fields.id'],
            name='fk_field_id_metadata_values'
        ),
        sa.ForeignKeyConstraint(
            ['product_id'], ['products.id'],
            name='fk_product_id_metadata_values'
        ),
        sa.UniqueConstraint(
            'field_id', 'product_id',
            name='u_field_id_product_id'
        )
    )


def downgrade():
    op.drop_table('metadata_values')
    op.drop_table('metadata_fields')
    op.drop_table('cart_items')
    op.drop_table('products')
    op.drop_table('categories')
    op.drop_table('sectors')
    op.drop_table('departments')
    op.drop_table('carts')
