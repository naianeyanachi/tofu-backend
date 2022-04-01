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


class Cart(DeclarativeBase):
    __tablename__ = "carts"

    id = Column(String, primary_key=True)
    user_id = Column(String)
    name = Column(String)
    cart_items = relationship("CartItem", cascade="delete")


class SectorDepartment(DeclarativeBase):
    __tablename__ = 'sector_department'
    id = Column(String, primary_key=True)
    sector_id = Column(ForeignKey('sectors.id', name='fk_sector_id_sector_department'))
    department_id = Column(ForeignKey('departments.id', name='fk_department_id_sector_department'))
    department = relationship("Department", back_populates="sectors")
    sector = relationship("Sector", back_populates="departments")


class CategorySector(DeclarativeBase):
    __tablename__ = 'category_sector'
    id = Column(String, primary_key=True)
    sector_id = Column(ForeignKey('sectors.id', name='fk_sector_id_category_sector'))
    category_id = Column(ForeignKey('categories.id', name='fk_category_id_category_sector'))
    category = relationship("Category", back_populates="sectors")
    sector = relationship("Sector", back_populates="categories")


class Department(DeclarativeBase):
    __tablename__ = "departments"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    sectors = relationship("SectorDepartment", back_populates="department")


class Sector(DeclarativeBase):
    __tablename__ = "sectors"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    departments = relationship("SectorDepartment", back_populates="sector")
    categories = relationship("CategorySector", back_populates="sector")


class Category(DeclarativeBase):
    __tablename__ = "categories"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    sectors = relationship("CategorySector", back_populates="category")


class Product(DeclarativeBase):
    __tablename__ = "products"

    id = Column(String, primary_key=True)
    sku = Column(String)
    description = Column(String, nullable=False)
    category_id = Column(
        String,
        ForeignKey("categories.id", name="fk_category_id_products"),
        nullable=False
    )
    values = relationship("MetadataValue")
    category = relationship("Category")


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
    product = relationship("Product", uselist=False)
    cart = relationship("Cart", uselist=False)


class MetadataField(DeclarativeBase):
    __tablename__ = "metadata_fields"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)


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
    field = relationship("MetadataField", uselist=False)
