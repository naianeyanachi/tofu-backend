import json
import logging

from marshmallow import ValidationError
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from gateway.entrypoints import http
from gateway.exceptions import CartNotFound
from gateway.schemas import (AddProductsSchema, CartSchema, CategorySchema,
                             CreateCartSchema, ProductSchema)


class GatewayService(object):
    """
    Service acts as a gateway to other services over http.
    """

    name = 'gateway'

    carts_rpc = RpcProxy('carts')

    @http("GET", "/cart/<string:cart_id>", expected_exceptions=CartNotFound)
    def get_cart(self, request, cart_id):  # OK
        cart = self.carts_rpc.get_cart(cart_id)
        return Response(
            CartSchema().dumps(cart).data,
            mimetype='application/json'
        )

    @http("GET", "/users/<string:user_id>/carts", expected_exceptions=CartNotFound)
    def get_cart_by_user(self, request, user_id):  # OK
        cart = self.carts_rpc.get_carts_by_user(user_id)
        return Response(
            CartSchema(many=True).dumps(cart).data,
            mimetype='application/json'
        )

    @http("GET", "/categories/<string:term>", expected_exceptions=CartNotFound)
    def get_categories_by_term(self, request, term):  # OK
        cart_collection = self.carts_rpc.get_categories_by_term(term)
        return Response(
            CategorySchema(many=True).dumps(cart_collection).data,
            mimetype='application/json'
        )

    @http("GET", "/category/<string:category_id>/products", expected_exceptions=CartNotFound)
    def get_products_by_category(self, request, category_id):  # OK
        product_collection = self.carts_rpc.get_products_by_category(category_id)
        return Response(
            ProductSchema(many=True).dumps(product_collection).data,
            mimetype='application/json'
        )

    @http("POST", "/cart", expected_exceptions=(ValidationError, BadRequest))
    def create_cart(self, request):  # OK
        schema = CreateCartSchema(strict=True)

        try:
            cart_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = CreateCartSchema().dump(cart_data).data
        result = self.carts_rpc.create_cart(
            serialized_data['user_id']
        )
        return Response(
            json.dumps({'id': result['id']}),
            mimetype='application/json'
        )

    @http("POST", "/cart/<string:cart_id>/products", expected_exceptions=(ValidationError, BadRequest))
    def add_products_to_cart(self, request, cart_id):
        schema = AddProductsSchema(strict=True)

        try:
            product_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = AddProductsSchema().dump(product_data).data
        self.carts_rpc.add_products_to_cart(
            cart_id,
            serialized_data['category_id'],
            serialized_data['product_ids'],
            serialized_data['quantity']
        )

        return 'success'

    @http("DELETE", "/cart/<string:cart_id>", expected_exceptions=CartNotFound)
    def delete_cart(self, request, cart_id):  # OK
        self.carts_rpc.delete_cart(cart_id)
        return 'success'

    # @http(
    #     "POST", "/orders",
    #     expected_exceptions=(ValidationError, ProductNotFound, BadRequest)
    # )
    # def create_order(self, request):
    #     """Create a new order - order data is posted as json

    #     Example request ::

    #         {
    #             "order_details": [
    #                 {
    #                     "product_id": "the_odyssey",
    #                     "price": "99.99",
    #                     "quantity": 1
    #                 },
    #                 {
    #                     "price": "5.99",
    #                     "product_id": "the_enigma",
    #                     "quantity": 2
    #                 },
    #             ]
    #         }

    #     The response contains the new order ID in a json document ::

    #         {"id": 1234}

    #     """

    #     schema = CreateOrderSchema(strict=True)

    #     try:
    #         # load input data through a schema (for validation)
    #         # Note - this may raise `ValueError` for invalid json,
    #         # or `ValidationError` if data is invalid.
    #         order_data = schema.loads(request.get_data(as_text=True)).data
    #     except ValueError as exc:
    #         raise BadRequest("Invalid json: {}".format(exc))

    #     # Create the order
    #     # Note - this may raise `ProductNotFound`
    #     id_ = self._create_order(order_data)
    #     return Response(json.dumps({'id': id_}), mimetype='application/json')

    # def _create_order(self, order_data):
    #     # check order product ids are valid
    #     valid_product_ids = {prod['id'] for prod in self.products_rpc.list()}
    #     for item in order_data['order_details']:
    #         if item['product_id'] not in valid_product_ids:
    #             raise ProductNotFound(
    #                 "Product Id {}".format(item['product_id'])
    #             )

    #     # Call orders-service to create the order.
    #     # Dump the data through the schema to ensure the values are serialized
    #     # correctly.
    #     serialized_data = CreateOrderSchema().dump(order_data).data
    #     result = self.orders_rpc.create_order(
    #         serialized_data['order_details']
    #     )
    #     return result['id']
