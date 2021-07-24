"""mock

Revision ID: a0ee11c88d5d
Revises: dd33cb03d01f
Create Date: 2021-07-24 13:51:31.034548

"""

# revision identifiers, used by Alembic.
revision = 'a0ee11c88d5d'
down_revision = 'dd33cb03d01f'
branch_labels = None
depends_on = None

import datetime
from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, DateTime, DECIMAL
import sqlalchemy as sa

users_table = table('users',
    column('id', String),
    column('name', String),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)
carts_table = table('carts',
    column('id', String),
    column('user_id', String),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)
categories_table = table('categories',
    column('id', String),
    column('name', String),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)
products_table = table('products',
    column('id', String),
    column('category_id', String),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)
cart_items_table = table('cart_items',
    column('id', String),
    column('cart_id', String),
    column('product_id', String),
    column('quantity', DECIMAL),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)
metadata_fields_table = table('metadata_fields',
    column('id', Integer),
    column('field', String),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)
metadata_values_table = table('metadata_values',
    column('id', String),
    column('field_id', String),
    column('product_id', String),
    column('value', String),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)

def upgrade():
    op.bulk_insert(users_table,
        [
            {
                'id': 'naiane',
                'name': 'naiane',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'emoji',
                'name': 'emoji',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )
    op.bulk_insert(carts_table,
        [
            {
                'id': 'cart_1',
                'user_id': 'naiane',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'cart_2',
                'user_id': 'emoji',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )
    op.bulk_insert(categories_table,
        [
            {
                'id': 'category_1',
                'name': 'salgadinho',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'category_2',
                'name': 'chocolate',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'category_3',
                'name': 'leite condensado',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'category_4',
                'name': 'cabo de vassoura',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )
    op.bulk_insert(products_table,
        [
            {
                'id': 'product_10',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_11',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_12',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_13',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_14',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_15',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_16',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_17',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_18',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_19',
                'category_id': 'category_1',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_20',
                'category_id': 'category_2',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_21',
                'category_id': 'category_2',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_22',
                'category_id': 'category_2',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_23',
                'category_id': 'category_2',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_24',
                'category_id': 'category_2',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_25',
                'category_id': 'category_2',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_30',
                'category_id': 'category_3',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_31',
                'category_id': 'category_3',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_40',
                'category_id': 'category_4',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'product_41',
                'category_id': 'category_4',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )
    op.bulk_insert(cart_items_table,
        [
            {
                'id': 'item_10',
                'cart_id': 'cart_1',
                'product_id': 'product_10',
                'quantity': 1.0,
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'item_20',
                'cart_id': 'cart_2',
                'product_id': 'product_17',
                'quantity': 1.0,
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'item_21',
                'cart_id': 'cart_2',
                'product_id': 'product_30',
                'quantity': 1.0,
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )
    op.bulk_insert(metadata_fields_table,
        [
            {
                'id': 'size',
                'field': 'size',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'brand',
                'field': 'brand',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'color',
                'field': 'color',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'flavor',
                'field': 'flavor',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )
    op.bulk_insert(metadata_values_table,
        [
            {
                'id': 'value_01',
                'field_id': 'size',
                'product_id': 'product_10',
                'value': '100g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_02',
                'field_id': 'brand',
                'product_id': 'product_10',
                'value': 'lays',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_03',
                'field_id': 'flavor',
                'product_id': 'product_10',
                'value': 'queijo',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_04',
                'field_id': 'size',
                'product_id': 'product_11',
                'value': '100g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_05',
                'field_id': 'brand',
                'product_id': 'product_11',
                'value': 'lays',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_06',
                'field_id': 'flavor',
                'product_id': 'product_11',
                'value': 'vinagre',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_07',
                'field_id': 'size',
                'product_id': 'product_12',
                'value': '100g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_08',
                'field_id': 'brand',
                'product_id': 'product_12',
                'value': 'lays',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_09',
                'field_id': 'flavor',
                'product_id': 'product_12',
                'value': 'churrasco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_10',
                'field_id': 'size',
                'product_id': 'product_13',
                'value': '100g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_11',
                'field_id': 'brand',
                'product_id': 'product_13',
                'value': 'lays',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_12',
                'field_id': 'flavor',
                'product_id': 'product_13',
                'value': 'tradicional',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_13',
                'field_id': 'size',
                'product_id': 'product_14',
                'value': '100g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_14',
                'field_id': 'brand',
                'product_id': 'product_14',
                'value': 'lays',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_15',
                'field_id': 'flavor',
                'product_id': 'product_14',
                'value': 'onion',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_16',
                'field_id': 'size',
                'product_id': 'product_15',
                'value': '200g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_17',
                'field_id': 'brand',
                'product_id': 'product_15',
                'value': 'lays',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_18',
                'field_id': 'flavor',
                'product_id': 'product_15',
                'value': 'tradicional',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_22',
                'field_id': 'size',
                'product_id': 'product_16',
                'value': '150g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_23',
                'field_id': 'brand',
                'product_id': 'product_16',
                'value': 'ruffles',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_24',
                'field_id': 'flavor',
                'product_id': 'product_16',
                'value': 'tradicional',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_25',
                'field_id': 'size',
                'product_id': 'product_17',
                'value': '150g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_26',
                'field_id': 'brand',
                'product_id': 'product_17',
                'value': 'ruffles',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_27',
                'field_id': 'flavor',
                'product_id': 'product_17',
                'value': 'churrasco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_28',
                'field_id': 'size',
                'product_id': 'product_18',
                'value': '250g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_29',
                'field_id': 'brand',
                'product_id': 'product_18',
                'value': 'ruffles',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_30',
                'field_id': 'flavor',
                'product_id': 'product_18',
                'value': 'tradicional',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_31',
                'field_id': 'size',
                'product_id': 'product_19',
                'value': '100g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_32',
                'field_id': 'brand',
                'product_id': 'product_19',
                'value': 'doritos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_33',
                'field_id': 'flavor',
                'product_id': 'product_19',
                'value': 'tradicional',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_34',
                'field_id': 'size',
                'product_id': 'product_20',
                'value': '90g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_35',
                'field_id': 'brand',
                'product_id': 'product_20',
                'value': 'nestlé',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_36',
                'field_id': 'flavor',
                'product_id': 'product_20',
                'value': 'leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_37',
                'field_id': 'size',
                'product_id': 'product_21',
                'value': '90g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_38',
                'field_id': 'brand',
                'product_id': 'product_21',
                'value': 'nestlé',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_39',
                'field_id': 'flavor',
                'product_id': 'product_21',
                'value': 'amargo',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_40',
                'field_id': 'size',
                'product_id': 'product_22',
                'value': '90g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_41',
                'field_id': 'brand',
                'product_id': 'product_22',
                'value': 'nestlé',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_42',
                'field_id': 'flavor',
                'product_id': 'product_22',
                'value': 'branco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_43',
                'field_id': 'size',
                'product_id': 'product_23',
                'value': '90g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_44',
                'field_id': 'brand',
                'product_id': 'product_23',
                'value': 'lacta',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_45',
                'field_id': 'flavor',
                'product_id': 'product_23',
                'value': 'laka',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_46',
                'field_id': 'size',
                'product_id': 'product_24',
                'value': '90g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_47',
                'field_id': 'brand',
                'product_id': 'product_24',
                'value': 'lacta',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_48',
                'field_id': 'flavor',
                'product_id': 'product_24',
                'value': 'diamante negro',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_49',
                'field_id': 'size',
                'product_id': 'product_25',
                'value': '90g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_50',
                'field_id': 'brand',
                'product_id': 'product_25',
                'value': 'lacta',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_51',
                'field_id': 'flavor',
                'product_id': 'product_25',
                'value': 'confeti',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_52',
                'field_id': 'size',
                'product_id': 'product_30',
                'value': '200g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_53',
                'field_id': 'brand',
                'product_id': 'product_30',
                'value': 'nestlé',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_54',
                'field_id': 'size',
                'product_id': 'product_31',
                'value': '200g',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_55',
                'field_id': 'brand',
                'product_id': 'product_31',
                'value': 'triângulo',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_56',
                'field_id': 'color',
                'product_id': 'product_40',
                'value': 'azul',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'value_57',
                'field_id': 'color',
                'product_id': 'product_41',
                'value': 'verde',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )


def downgrade():
    op.execute('DELETE FROM metadata_values')
    op.execute('DELETE FROM metadata_fields')
    op.execute('DELETE FROM cart_items')
    op.execute('DELETE FROM products')
    op.execute('DELETE FROM categories')
    op.execute('DELETE FROM carts')
    op.execute('DELETE FROM users')
