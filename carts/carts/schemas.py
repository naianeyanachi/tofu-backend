from marshmallow import Schema, fields


class CartItemSchema(Schema):
    id = fields.Str(required=True)
    cart_id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    quantity = fields.Decimal(required=True)


class CartSchema(Schema):
    id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    cart_items = fields.Nested(CartItemSchema, many=True)


class CategorySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)


class ProductSchema(Schema):
    id = fields.Str(required=True)
    category_id = fields.Str(required=True)
