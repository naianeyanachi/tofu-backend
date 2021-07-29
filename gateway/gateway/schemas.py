from marshmallow import Schema, fields


class CreateCartSchema(Schema):
    user_id = fields.Str(required=True)


class AddProductIdSchema(Schema):
    product_id = fields.Str(required=True)


class AddProductsSchema(Schema):
    product_ids = fields.Nested(AddProductIdSchema, many=True)
    category_id = fields.Str(required=True)
    quantity = fields.Decimal(as_string=True)


class RemoveProductsSchema(Schema):
    category_id = fields.Str(required=True)


class MetadataFieldSchema(Schema):
    __tablename__ = "metadata_values"

    id = fields.Str(required=True)
    field = fields.Str(required=True)


class MetadataValueSchema(Schema):
    __tablename__ = "metadata_values"

    id = fields.Str(required=True)
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
    quantity = fields.Decimal(required=True, as_string=True)
    product = fields.Nested(ProductSchema)


class CartSchema(Schema):
    id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    cart_items = fields.Nested(CartItemSchema, many=True)


class SearchSchema(Schema):
    user_id = fields.Str(required=True)
    cart_items = fields.Nested(CartItemSchema, many=True)
