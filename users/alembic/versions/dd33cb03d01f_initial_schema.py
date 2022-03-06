"""initial schema

Revision ID: dd33cb03d01f
Revises:
Create Date: 2021-07-23 13:51:31.034548

"""

import sqlalchemy as sa
from sqlalchemy.sql import column, table
from alembic import op

# revision identifiers, used by Alembic.
revision = 'dd33cb03d01f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "authentication",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),

        sa.PrimaryKeyConstraint("id"),
    )

    authentication_table = table('authentication',
        column('id', sa.Integer),
        column('type', sa.String),
    )
    op.bulk_insert(authentication_table,
        [
            {
                'id': 1,
                'type': 'password',
            },
            {
                'id': 2,
                'type': 'google',
            },
            {
                'id': 3,
                'type': 'facebook',
            },
        ]
    )

    op.create_table(
        "users",
        sa.Column("id", sa.String(), nullable=False, unique=True),
        sa.Column("external_id", sa.String(), nullable=True),
        sa.Column("authentication_id", sa.Integer(), nullable=False),
        sa.Column("pwd_hash", sa.String(), nullable=True),
        sa.Column("pwd_salt", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False, unique=True),
        sa.Column("phone", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),

        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["authentication_id"], ["authentication.id"],
            name="fk_authentication_id_users"
        ),
    )
    
    op.create_table(
        "addresses",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("number", sa.String(), nullable=False),
        sa.Column("complement", sa.String(), nullable=False),
        sa.Column("cep", sa.Integer(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),

        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"],
            name="fk_user_id_addresses"
        ),
    )



def downgrade():
    op.drop_table("addresses")
    op.drop_table("authentication")
    op.drop_table("users")
