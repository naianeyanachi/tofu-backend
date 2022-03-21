from marshmallow import Schema, fields


class CreateCartSchema(Schema):
    user_id = fields.Str(required=True)
    name = fields.Str(required=True)


class RenameCartSchema(Schema):
    name = fields.Str(required=True)


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
    name = fields.Str(required=True)
    cart_items = fields.Nested(CartItemSchema, many=True)


class SearchSchema(Schema):
    user_id = fields.Str(required=True)
    cart_items = fields.Nested(CartItemSchema, many=True)


class CartHistorySchema(Schema):
    id = fields.Str(required=True)
    cart_items = fields.Nested(CartItemSchema, many=True)


class SearchHistorySchema(Schema):
    id = fields.Str(required=True)
    created_at = fields.Str(required=True)
    cart = fields.Nested(CartHistorySchema)


class CreatePasswordUserSchema(Schema):
    pwd_hash = fields.Str(required=True)
    pwd_salt = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)


class CreateAddressSchema(Schema):
    address = fields.Str(required=False)
    number = fields.Str(required=True)
    complement = fields.Str(required=True)
    cep = fields.Int(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)


class AuthenticationSchema(Schema):
    id = fields.Str(required=True)
    type = fields.Str(required=True)


class AddressSchema(Schema):
    id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    address = fields.Str(required=False)
    number = fields.Str(required=True)
    complement = fields.Str(required=True)
    cep = fields.Int(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)


class UserSchema(Schema):
    id = fields.Str(required=True)
    external_id = fields.Str(required=True)
    authentication_id = fields.Str(required=False)
    pwd_hash = fields.Str(required=True)
    pwd_salt = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=False)

    authentication = fields.Nested(AuthenticationSchema)
    addresses = fields.Nested(AddressSchema, many=True)
