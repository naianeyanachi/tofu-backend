import datetime

from sqlalchemy import DECIMAL, Column, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )


DeclarativeBase = declarative_base(cls=Base)


class Search(DeclarativeBase):
    __tablename__ = "searches"

    id = Column(String, primary_key=True)
    cart_id = Column(
        String,
        ForeignKey("carts.id", name="fk_cart_id_carts"),
        nullable=False
    )
    cart = relationship("Cart")


class Cart(DeclarativeBase):
    __tablename__ = "carts"

    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    cart_items = relationship("CartItem", cascade="merge")


class Category(DeclarativeBase):
    __tablename__ = "categories"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)


class Product(DeclarativeBase):
    __tablename__ = "products"

    id = Column(String, primary_key=True)
    category_id = Column(
        String,
        ForeignKey("categories.id", name="fk_category_id_products"),
        nullable=False
    )
    category = relationship("Category", cascade="merge")
    values = relationship("MetadataValue", cascade="merge")


class CartItem(DeclarativeBase):
    __tablename__ = "cart_items"

    id = Column(String, primary_key=True)
    cart_id = Column(
        String,
        ForeignKey("carts.id", name="fk_cart_id_cart_items"),
        nullable=False
    )
    product_id = Column(
        String,
        ForeignKey("products.id", name="fk_product_id_cart_items"),
        nullable=False
    )
    quantity = Column(DECIMAL, nullable=False)
    product = relationship("Product", uselist=False, cascade="merge")


class MetadataField(DeclarativeBase):
    __tablename__ = "metadata_fields"

    id = Column(String, primary_key=True)
    field = Column(String, nullable=False)


class MetadataValue(DeclarativeBase):
    __tablename__ = "metadata_values"

    id = Column(String, primary_key=True)
    field_id = Column(
        String,
        ForeignKey("metadata_fields.id", name="fk_field_id_metadata_value"),
        nullable=False
    )
    product_id = Column(
        String,
        ForeignKey("products.id", name="fk_user_id_carts"),
        nullable=False
    )
    value = Column(String, nullable=False)
    field = relationship("MetadataField", uselist=False, cascade="merge")
