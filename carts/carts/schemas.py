from marshmallow import Schema, fields


class OrderDetailSchema(Schema):
    id = fields.Int(required=True)
    product_id = fields.Str(required=True)
    price = fields.Decimal(as_string=True)
    quantity = fields.Int()


class OrderSchema(Schema):
    id = fields.Int(required=True)
    order_details = fields.Nested(OrderDetailSchema, many=True)


class CartItemSchema(Schema):
    id = fields.Str(required=True)
    cart_id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    quantity = fields.Decimal(required=True)


class CartSchema(Schema):
    id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    cart_items = fields.Nested(CartItemSchema, many=True)


class CartsCollectionSchema(Schema):
    carts = fields.Nested(CartSchema, many=True)


class CategorySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)


class CategoryCollectionSchema(Schema):
    categories = fields.Nested(CategorySchema, many=True)


class ProductSchema(Schema):
    id = fields.Str(required=True)
    category_id = fields.Str(required=True)


class ProductCollectionSchema(Schema):
    products = fields.Nested(ProductSchema, many=True)