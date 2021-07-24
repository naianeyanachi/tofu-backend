from marshmallow import Schema, fields


class CartSchema(Schema):
    id = fields.Str()
    user_id = fields.Str()


class CategorySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    

class ProductSchema(Schema):
    id = fields.Str(required=True)
    category_id = fields.Str(required=True)
