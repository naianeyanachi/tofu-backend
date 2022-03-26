import logging

from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from nanoid import generate

from admin_carts.exceptions import NotFound
from admin_carts.models import (Category, CategorySector, DeclarativeBase,
                                Department, Sector, SectorDepartment, MetadataValue, Product)
from admin_carts.schemas import DepartmentSchema, ProductSchema


class AdminCartsService:
    name = 'admin_carts'

    db = DatabaseSession(DeclarativeBase)

    @rpc
    def get_all_departments(self):
        department = self.db.query(Department).join(
            SectorDepartment,
            SectorDepartment.department_id == Department.id,
            isouter=True
        ).join(
            Sector,
            Sector.id == SectorDepartment.sector_id,
            isouter=True
        ).join(
            CategorySector,
            CategorySector.sector_id == Sector.id,
            isouter=True
        ).join(
            Category,
            Category.id == CategorySector.category_id,
            isouter=True
        ).all()

        if not department:
            raise NotFound('Cart not found')

        return DepartmentSchema(many=True).dump(department).data

    @rpc
    def get_products_by_category(self, category_id):
        products = self.db.query(Product).filter(Product.category_id == category_id).all()

        if not products:
            raise NotFound('Products not found')

        return ProductSchema(many=True).dump(products).data

    @rpc
    def bulk_create_departments(self, names):
        for name in names:
            department = Department(id=generate(), name=name)
            self.db.add(department)
        self.db.commit()

        return self.get_all_departments()

    @rpc
    def bulk_create_sectors(self, department_id, names):
        for name in names:
            sector_id = generate()
            sectors = Sector(
                id=sector_id,
                name=name
            )
            sector_department = SectorDepartment(
                id=generate(),
                department_id=department_id,
                sector_id=sector_id
            )
            self.db.add(sectors)
            self.db.add(sector_department)
        self.db.commit()

        return self.get_all_departments()

    @rpc
    def bulk_create_categories(self, sector_id, names):
        for name in names:
            category_id = generate()
            sectors = Category(
                id=category_id,
                name=name
            )
            category_sector = CategorySector(
                id=generate(),
                category_id=category_id,
                sector_id=sector_id
            )
            self.db.add(sectors)
            self.db.add(category_sector)
        self.db.commit()

        return self.get_all_departments()

    @rpc
    def bulk_create_products(self, category_id, products):
        for product in products:
            product_id = generate()
            insert_product = Product(
                id=product_id,
                category_id=category_id,
                description=product['description'],
                sku=product['sku']
            )
            self.db.add(insert_product)
            for value in product['values']:
                insert_value = MetadataValue(
                    id=generate(),
                    field_id=value['field_id'],
                    product_id=product_id,
                    value=value['value']
                )
                self.db.add(insert_value)
        self.db.commit()

        return self.get_products_by_category(category_id)
