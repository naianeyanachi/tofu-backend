from marshmallow import Schema, fields


class CreateCartSchema(Schema):
    user_id = fields.Str()


class CartSchema(Schema):
    id = fields.Str()
    user_id = fields.Str()


class CategorySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)


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


class ProductSchema(Schema):
    id = fields.Str(required=True)
    category_id = fields.Str(required=True)
    values = fields.Nested(MetadataValueSchema, many=True)
