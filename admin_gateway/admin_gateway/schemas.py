from marshmallow import Schema, fields


class MetadataFieldSchema(Schema):
    __tablename__ = "metadata_values"

    id = fields.Str(required=True)
    name = fields.Str(required=True)


class MetadataValueSchema(Schema):
    __tablename__ = "metadata_values"

    id = fields.Str(required=True)
    field_id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    value = fields.Str(required=True)
    field = fields.Nested(MetadataFieldSchema)


class CategorySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)


class CategorySectorSchema(Schema):
    id = fields.Str(required=True)
    sector_id = fields.Str(required=True)
    category_id = fields.Str(required=True)
    category = fields.Nested(CategorySchema)


class SectorSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    categories = fields.Nested(CategorySectorSchema, many=True)


class SectorDepartmentSchema(Schema):
    id = fields.Str(required=True)
    sector_id = fields.Str(required=True)
    department_id = fields.Str(required=True)
    sector = fields.Nested(SectorSchema)


class DepartmentSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    sectors = fields.Nested(SectorDepartmentSchema, many=True)


class ProductSchema(Schema):
    id = fields.Str(required=True)
    category_id = fields.Str(required=True)
    sku = fields.Str(required=True)
    description = fields.Str(required=True)
    category = fields.Nested(CategorySchema)
    values = fields.Nested(MetadataValueSchema, many=True)


class CartItemSchema(Schema):
    id = fields.Str(required=True)
    cart_id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    quantity = fields.Decimal(required=True)
    product = fields.Nested(ProductSchema)


class CartSchema(Schema):
    id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    name = fields.Str(required=True)
    cart_items = fields.Nested(CartItemSchema, many=True)


class BulkCreateDepartments(Schema):
    names = fields.List(fields.Str(), required=True)


class BulkCreateSectors(Schema):
    department_id = fields.Str(required=True)
    names = fields.List(fields.Str(), required=True)


class BulkCreateCategories(Schema):
    sector_id = fields.Str(required=True)
    names = fields.List(fields.Str(), required=True)


class BulkCreateProductMetadataValueSchema(Schema):
    field_id = fields.Str(required=True)
    value = fields.Str(required=True)


class BulkCreateProductSchema(Schema):
    sku = fields.Str(required=True)
    description = fields.Str(required=True)
    values = fields.Nested(BulkCreateProductMetadataValueSchema, many=True)


class BulkCreateProducts(Schema):
    category_id = fields.Str(required=True)
    products = fields.Nested(BulkCreateProductSchema, many=True)
