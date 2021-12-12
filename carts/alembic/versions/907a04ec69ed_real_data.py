"""mock

Revision ID: 907a04ec69ed
Revises: 23ceceeeb9ee
Create Date: 2021-07-24 13:51:31.034548

"""

# revision identifiers, used by Alembic.
revision = '907a04ec69ed'
down_revision = '23ceceeeb9ee'
branch_labels = None
depends_on = None

import datetime

from alembic import op
from sqlalchemy import DECIMAL, DateTime, Integer, String
from sqlalchemy.sql import column, table

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
metadata_values_table = table('metadata_values',
    column('id', String),
    column('field_id', String),
    column('product_id', String),
    column('value', String),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)


def upgrade():
    op.bulk_insert(categories_table,
        [
            {
                'id': 'real_ovos',
                'name': 'ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite',
                'name': 'leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao',
                'name': 'pão',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco',
                'name': 'suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz',
                'name': 'arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne',
                'name': 'carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga',
                'name': 'manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )
    op.bulk_insert(products_table,
        [
            {
                'id': 'real_ovos_02',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_03',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_04',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_05',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_06',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_07',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_08',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_09',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_10',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_11',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_12',
                'category_id': 'real_ovos',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_01',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_02',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_03',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_04',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_05',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_06',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_07',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_08',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_09',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_10',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_11',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_12',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_13',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_14',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_15',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_16',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_17',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_18',
                'category_id': 'real_leite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_01',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_02',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_03',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_04',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_05',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_06',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_07',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_08',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_09',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_10',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_11',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_12',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_13',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_14',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_15',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_16',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_17',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_18',
                'category_id': 'real_pao',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_01',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_02',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_03',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_04',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_05',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_06',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_07',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_08',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_09',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_10',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_11',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_12',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_13',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_14',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_15',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_16',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_17',
                'category_id': 'real_suco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_01',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_02',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_03',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_04',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_05',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_06',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_07',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_08',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_09',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_10',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_11',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_12',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_13',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_14',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_15',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_16',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_17',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_18',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_19',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_20',
                'category_id': 'real_arroz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_01',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_02',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_03',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_04',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_05',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_06',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_07',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_08',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_09',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_10',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_11',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_12',
                'category_id': 'real_carne',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_01',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_02',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_03',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_04',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_05',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_06',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_07',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_08',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_09',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_10',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_11',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_12',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_13',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_14',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_15',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_16',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_17',
                'category_id': 'real_manteiga',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )
    op.bulk_insert(metadata_values_table,
        [
            {
                'id': 'real_ovos_02',
                'field_id': 'brand',
                'product_id': 'real_ovos_02',
                'value': 'Bechtle',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_03',
                'field_id': 'brand',
                'product_id': 'real_ovos_03',
                'value': 'Manischewitz',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_04',
                'field_id': 'brand',
                'product_id': 'real_ovos_04',
                'value': 'Amish Kitchens',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_05',
                'field_id': 'brand',
                'product_id': 'real_ovos_05',
                'value': 'Al Dente',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_06',
                'field_id': 'brand',
                'product_id': 'real_ovos_06',
                'value': 'Blue Dragon',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_07',
                'field_id': 'brand',
                'product_id': 'real_ovos_07',
                'value': 'Cipriani',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_08',
                'field_id': 'brand',
                'product_id': 'real_ovos_08',
                'value': 'CosterStone',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_09',
                'field_id': 'brand',
                'product_id': 'real_ovos_09',
                'value': 'DeLallo',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_10',
                'field_id': 'brand',
                'product_id': 'real_ovos_10',
                'value': 'Kikkoman',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_11',
                'field_id': 'brand',
                'product_id': 'real_ovos_11',
                'value': 'LesserEvil',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_ovos_12',
                'field_id': 'brand',
                'product_id': 'real_ovos_12',
                'value': 'Trolli',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_01',
                'field_id': 'brand',
                'product_id': 'real_leite_01',
                'value': 'Blue Diamond',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_02',
                'field_id': 'brand',
                'product_id': 'real_leite_02',
                'value': 'Pacific Foods',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_03',
                'field_id': 'brand',
                'product_id': 'real_leite_03',
                'value': 'Chocolove',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_04',
                'field_id': 'brand',
                'product_id': 'real_leite_04',
                'value': 'Traditional Medicinals',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_05',
                'field_id': 'brand',
                'product_id': 'real_leite_05',
                'value': 'Natural Value',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_06',
                'field_id': 'brand',
                'product_id': 'real_leite_06',
                'value': 'Bahlsen',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_07',
                'field_id': 'brand',
                'product_id': 'real_leite_07',
                'value': 'Enfamil',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_08',
                'field_id': 'brand',
                'product_id': 'real_leite_08',
                'value': 'CosterStone',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_09',
                'field_id': 'brand',
                'product_id': 'real_leite_09',
                'value': 'Theo Chocolate',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_10',
                'field_id': 'brand',
                'product_id': 'real_leite_10',
                'value': 'Celebration Herbals',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_11',
                'field_id': 'brand',
                'product_id': 'real_leite_11',
                'value': 'KA-ME',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_12',
                'field_id': 'brand',
                'product_id': 'real_leite_12',
                'value': 'Lindt',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_13',
                'field_id': 'brand',
                'product_id': 'real_leite_13',
                'value': 'Alvita Teas',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_14',
                'field_id': 'brand',
                'product_id': 'real_leite_14',
                'value': 'Dream',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_15',
                'field_id': 'brand',
                'product_id': 'real_leite_15',
                'value': 'Endangered Species',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_16',
                'field_id': 'brand',
                'product_id': 'real_leite_16',
                'value': 'Mars',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_17',
                'field_id': 'brand',
                'product_id': 'real_leite_17',
                'value': 'Russell Stover',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_leite_18',
                'field_id': 'brand',
                'product_id': 'real_leite_18',
                'value': 'Southern Gourmet',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_01',
                'field_id': 'brand',
                'product_id': 'real_pao_01',
                'value': 'Rastelli\'s',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_02',
                'field_id': 'brand',
                'product_id': 'real_pao_02',
                'value': 'Zatarains',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_03',
                'field_id': 'brand',
                'product_id': 'real_pao_03',
                'value': 'reShore Lunchal',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_04',
                'field_id': 'brand',
                'product_id': 'real_pao_04',
                'value': 'Kikkoman',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_05',
                'field_id': 'brand',
                'product_id': 'real_pao_05',
                'value': 'King Arthur Flour',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_06',
                'field_id': 'brand',
                'product_id': 'real_pao_06',
                'value': 'Louisiana Fish Fry',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_07',
                'field_id': 'brand',
                'product_id': 'real_pao_07',
                'value': 'Woodstock Farms',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_08',
                'field_id': 'brand',
                'product_id': 'real_pao_08',
                'value': 'Emeril Lagasse',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_09',
                'field_id': 'brand',
                'product_id': 'real_pao_09',
                'value': 'Chebe',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_10',
                'field_id': 'brand',
                'product_id': 'real_pao_10',
                'value': 'Hooters',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_11',
                'field_id': 'brand',
                'product_id': 'real_pao_11',
                'value': 'Red Star',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_12',
                'field_id': 'brand',
                'product_id': 'real_pao_12',
                'value': 'Osem',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_13',
                'field_id': 'brand',
                'product_id': 'real_pao_13',
                'value': 'Dean Jacob\'s',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_14',
                'field_id': 'brand',
                'product_id': 'real_pao_14',
                'value': 'ProBar',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_15',
                'field_id': 'brand',
                'product_id': 'real_pao_15',
                'value': 'Biscoff',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_16',
                'field_id': 'brand',
                'product_id': 'real_pao_16',
                'value': 'Alessi',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_17',
                'field_id': 'brand',
                'product_id': 'real_pao_17',
                'value': 'Bob\'s Red Mill',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_pao_18',
                'field_id': 'brand',
                'product_id': 'real_pao_18',
                'value': 'Crunchmaster',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_01',
                'field_id': 'brand',
                'product_id': 'real_suco_01',
                'value': 'Rastelli\'s',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_02',
                'field_id': 'brand',
                'product_id': 'real_suco_02',
                'value': 'Tropicana',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_03',
                'field_id': 'brand',
                'product_id': 'real_suco_03',
                'value': 'Santa Cruz Organic',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_04',
                'field_id': 'brand',
                'product_id': 'real_suco_04',
                'value': 'Knudsen',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_05',
                'field_id': 'brand',
                'product_id': 'real_suco_05',
                'value': 'IZZE',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_06',
                'field_id': 'brand',
                'product_id': 'real_suco_06',
                'value': 'Kedem',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_07',
                'field_id': 'brand',
                'product_id': 'real_suco_07',
                'value': 'Better Than Bouillon',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_08',
                'field_id': 'brand',
                'product_id': 'real_suco_08',
                'value': 'Lily of the Desert',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_09',
                'field_id': 'brand',
                'product_id': 'real_suco_09',
                'value': 'Bar Harbor',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_10',
                'field_id': 'brand',
                'product_id': 'real_suco_10',
                'value': 'Boscoli Family',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_11',
                'field_id': 'brand',
                'product_id': 'real_suco_11',
                'value': 'Campbell\'s',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_12',
                'field_id': 'brand',
                'product_id': 'real_suco_12',
                'value': 'Cento',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_13',
                'field_id': 'brand',
                'product_id': 'real_suco_13',
                'value': 'Cheribundi',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_14',
                'field_id': 'brand',
                'product_id': 'real_suco_14',
                'value': 'Frontier Herb',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_15',
                'field_id': 'brand',
                'product_id': 'real_suco_15',
                'value': 'Reese',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_16',
                'field_id': 'brand',
                'product_id': 'real_suco_16',
                'value': 'Master Of Mixes',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_suco_17',
                'field_id': 'brand',
                'product_id': 'real_suco_17',
                'value': 'McCormick',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_01',
                'field_id': 'brand',
                'product_id': 'real_arroz_01',
                'value': 'Lundberg Farms',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_02',
                'field_id': 'brand',
                'product_id': 'real_arroz_02',
                'value': 'Nakano',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_03',
                'field_id': 'brand',
                'product_id': 'real_arroz_03',
                'value': 'Sesmark',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_04',
                'field_id': 'brand',
                'product_id': 'real_arroz_04',
                'value': 'Alessi',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_05',
                'field_id': 'brand',
                'product_id': 'real_arroz_05',
                'value': 'Tasty Bite',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_06',
                'field_id': 'brand',
                'product_id': 'real_arroz_06',
                'value': 'Annie\'s Homegrown',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_07',
                'field_id': 'brand',
                'product_id': 'real_arroz_07',
                'value': 'Miracle Noodle',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_08',
                'field_id': 'brand',
                'product_id': 'real_arroz_08',
                'value': 'Beanfields',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_09',
                'field_id': 'brand',
                'product_id': 'real_arroz_09',
                'value': 'Vigo',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_10',
                'field_id': 'brand',
                'product_id': 'real_arroz_10',
                'value': 'Blue Diamond',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_11',
                'field_id': 'brand',
                'product_id': 'real_arroz_11',
                'value': 'Mahatma',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_12',
                'field_id': 'brand',
                'product_id': 'real_arroz_12',
                'value': 'Marukan',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_13',
                'field_id': 'brand',
                'product_id': 'real_arroz_13',
                'value': 'Lotus Foods',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_14',
                'field_id': 'brand',
                'product_id': 'real_arroz_14',
                'value': 'Annie Chun\'s',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_15',
                'field_id': 'brand',
                'product_id': 'real_arroz_15',
                'value': 'RiceSelect',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_16',
                'field_id': 'brand',
                'product_id': 'real_arroz_16',
                'value': 'A Taste of Thai',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_17',
                'field_id': 'brand',
                'product_id': 'real_arroz_17',
                'value': 'Tinkyada',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_18',
                'field_id': 'brand',
                'product_id': 'real_arroz_18',
                'value': 'KA-ME',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_19',
                'field_id': 'brand',
                'product_id': 'real_arroz_19',
                'value': 'Near East',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_arroz_20',
                'field_id': 'brand',
                'product_id': 'real_arroz_20',
                'value': 'Thai Kitchen',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_01',
                'field_id': 'brand',
                'product_id': 'real_carne_01',
                'value': 'Rastelli\'s',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_02',
                'field_id': 'brand',
                'product_id': 'real_carne_02',
                'value': 'Jack Link\'s',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_03',
                'field_id': 'brand',
                'product_id': 'real_carne_03',
                'value': 'Weber',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_04',
                'field_id': 'brand',
                'product_id': 'real_carne_04',
                'value': 'Badia',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_05',
                'field_id': 'brand',
                'product_id': 'real_carne_05',
                'value': 'Chef Merito',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_06',
                'field_id': 'brand',
                'product_id': 'real_carne_06',
                'value': 'Emeril Lagasse',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_07',
                'field_id': 'brand',
                'product_id': 'real_carne_07',
                'value': 'Frontera',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_08',
                'field_id': 'brand',
                'product_id': 'real_carne_08',
                'value': 'Kansas City Steak Company',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_09',
                'field_id': 'brand',
                'product_id': 'real_carne_09',
                'value': 'Spice Supreme',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_10',
                'field_id': 'brand',
                'product_id': 'real_carne_10',
                'value': 'The Spice Hunter',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_11',
                'field_id': 'brand',
                'product_id': 'real_carne_11',
                'value': 'Urban Accents',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_carne_12',
                'field_id': 'brand',
                'product_id': 'real_carne_12',
                'value': 'Watkins',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_01',
                'field_id': 'brand',
                'product_id': 'real_manteiga_01',
                'value': 'Rastelli\'s',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_02',
                'field_id': 'brand',
                'product_id': 'real_manteiga_02',
                'value': 'Woodstock Farms',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_03',
                'field_id': 'brand',
                'product_id': 'real_manteiga_03',
                'value': 'Clif Bar',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_04',
                'field_id': 'brand',
                'product_id': 'real_manteiga_04',
                'value': 'Peanut Butter & Co.',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_05',
                'field_id': 'brand',
                'product_id': 'real_manteiga_05',
                'value': 'Barney Butter',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_06',
                'field_id': 'brand',
                'product_id': 'real_manteiga_06',
                'value': 'ProBar',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_07',
                'field_id': 'brand',
                'product_id': 'real_manteiga_07',
                'value': 'GoMacro',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_08',
                'field_id': 'brand',
                'product_id': 'real_manteiga_08',
                'value': 'Sunbutter Natural',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_09',
                'field_id': 'brand',
                'product_id': 'real_manteiga_09',
                'value': 'Newman\'s Own',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_10',
                'field_id': 'brand',
                'product_id': 'real_manteiga_10',
                'value': 'Nabisco',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_11',
                'field_id': 'brand',
                'product_id': 'real_manteiga_11',
                'value': 'Office Snax',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_12',
                'field_id': 'brand',
                'product_id': 'real_manteiga_12',
                'value': 'Bob\'s Red Mill',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_13',
                'field_id': 'brand',
                'product_id': 'real_manteiga_13',
                'value': 'Dillman Farm',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_14',
                'field_id': 'brand',
                'product_id': 'real_manteiga_14',
                'value': 'Keebler',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_15',
                'field_id': 'brand',
                'product_id': 'real_manteiga_15',
                'value': 'Walkers Shortbread',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_16',
                'field_id': 'brand',
                'product_id': 'real_manteiga_16',
                'value': 'Act II',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': 'real_manteiga_17',
                'field_id': 'brand',
                'product_id': 'real_manteiga_17',
                'value': 'Annie\'s Homegrown',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )


def downgrade():
    op.execute('DELETE FROM metadata_values WHERE id like \'real_%\'')
    op.execute('DELETE FROM products WHERE id like \'real_%\'')
    op.execute('DELETE FROM categories WHERE id like \'real_%\'')
