from marshmallow import Schema, fields


class MetadataFieldSchema(Schema):
    __tablename__ = "metadata_values"

    id = fields.Str(required=True)
    field = fields.Str(required=True)


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


class ProductSchema(Schema):
    id = fields.Str(required=True)
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
    cart_items = fields.Nested(CartItemSchema, many=True)


class SearchSchema(Schema):
    id = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    cart = fields.Nested(CartSchema)
