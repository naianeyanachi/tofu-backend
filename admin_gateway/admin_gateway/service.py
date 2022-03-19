import json
import logging

from marshmallow import ValidationError
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from admin_gateway.entrypoints import http
from admin_gateway.exceptions import CartNotFound
# from admin_gateway.schemas import (AddProductsSchema, CartSchema, CategorySchema,
#                              CreateCartSchema, ProductSchema, RemoveProductsSchema,
#                              SearchSchema, SearchHistorySchema, RenameCartSchema,
#                              CreateAddressSchema, CreatePasswordUserSchema, UserSchema)


class AdminGatewayService(object):
    name = 'admin_gateway'

    admin_carts_rpc = RpcProxy('admin_carts')

    # CARTS SERVICE ------------------------------------------------------------------------

    @http("POST", "/department", expected_exceptions=(ValidationError, BadRequest))
    def get_cart(self, request):
        pass
        # schema = CreateCartSchema(strict=True)

        # try:
        #     department_data = schema.loads(request.get_data(as_text=True)).data
        # except ValueError:
        #     raise BadRequest("Invalid input")

        # serialized_data = CreateCartSchema().dump(department_data).data
        # result = self.carts_rpc.create_cart(
        #     serialized_data['user_id'],
        #     serialized_data['name']
        # )
        # return Response(
        #     json.dumps({'id': result['id']}),
        #     mimetype='application/json'
        # )
