"""initial schema

Revision ID: add14a4956c7
Revises: 
Create Date: 2021-08-07 23:27:33.645355

"""

# revision identifiers, used by Alembic.
revision = 'add14a4956c7'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "carts",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "searches",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("cart_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["cart_id"], ["carts.id"],
            name="fk_cart_id_carts"
        ),
    )

    op.create_table(
        "cart_items",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("cart_id", sa.String(), nullable=False),
        sa.Column("product_id", sa.String(), nullable=False),
        sa.Column("quantity", sa.DECIMAL(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["cart_id"], ["carts.id"],
            name="fk_cart_id_cart_items"
        ),
    )

def downgrade():
    op.drop_table("cart_items")
    op.drop_table("searches")
    op.drop_table("carts")
