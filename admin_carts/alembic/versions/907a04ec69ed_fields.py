"""fields

Revision ID: 907a04ec69ed
Revises: dd33cb03d01f
Create Date: 2021-07-24 13:51:31.034548

"""

# revision identifiers, used by Alembic.
revision = '907a04ec69ed'
down_revision = 'dd33cb03d01f'
branch_labels = None
depends_on = None

import datetime

from alembic import op
from nanoid import generate
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.sql import column, table

metadata_fields_table = table(
    'metadata_fields',
    column('id', Integer),
    column('name', String),
    column('created_at', DateTime),
    column('updated_at', DateTime),
)


def upgrade():
    op.bulk_insert(
        metadata_fields_table,
        [
            {
                'id': generate(),
                'name': 'size',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': generate(),
                'name': 'brand',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': generate(),
                'name': 'flavor',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
            {
                'id': generate(),
                'name': 'weight',
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            },
        ]
    )


def downgrade():
    op.execute('DELETE FROM metadata_fields')
