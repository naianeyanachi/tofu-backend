from marshmallow import Schema, fields


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

    addresses = fields.Nested(AddressSchema, many=True)


