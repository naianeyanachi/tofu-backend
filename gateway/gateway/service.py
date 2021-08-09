import json
import logging

from marshmallow import ValidationError
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from gateway.entrypoints import http
from gateway.exceptions import CartNotFound
from gateway.schemas import (AddProductsSchema, CartSchema, CategorySchema,
                             CreateCartSchema, ProductSchema, RemoveProductsSchema,
                             SearchSchema)


class GatewayService(object):
    """
    Service acts as a gateway to other services over http.
    """

    name = 'gateway'

    carts_rpc = RpcProxy('carts')
    search_rpc = RpcProxy('search')

    @http("GET", "/cart/<string:cart_id>", expected_exceptions=CartNotFound)
    def get_cart(self, _, cart_id):
        cart = self.carts_rpc.get_cart(cart_id)
        return Response(
            CartSchema().dumps(cart).data,
            mimetype='application/json'
        )

    @http("GET", "/users/<string:user_id>/carts", expected_exceptions=CartNotFound)
    def get_cart_by_user(self, _, user_id):
        cart = self.carts_rpc.get_carts_by_user(user_id)
        return Response(
            CartSchema(many=True).dumps(cart).data,
            mimetype='application/json'
        )

    @http("GET", "/categories/<string:term>", expected_exceptions=CartNotFound)
    def get_categories_by_term(self, _, term):
        cart_collection = self.carts_rpc.get_categories_by_term(term)
        return Response(
            CategorySchema(many=True).dumps(cart_collection).data,
            mimetype='application/json'
        )

    @http("GET", "/category/<string:category_id>/products", expected_exceptions=CartNotFound)
    def get_products_by_category(self, _, category_id):
        product_collection = self.carts_rpc.get_products_by_category(category_id)
        return Response(
            ProductSchema(many=True).dumps(product_collection).data,
            mimetype='application/json'
        )

    @http("POST", "/cart", expected_exceptions=(ValidationError, BadRequest))
    def create_cart(self, request):
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
    def delete_cart(self, _, cart_id):
        self.carts_rpc.delete_cart(cart_id)
        return 'success'

    @http("DELETE", "/cart/<string:cart_id>/products", expected_exceptions=CartNotFound)
    def remove_all_products_from_cart(self, _, cart_id):
        self.carts_rpc.remove_all_products_from_cart(cart_id)
        return 'success'

    @http("DELETE", "/cart/<string:cart_id>/category", expected_exceptions=CartNotFound)
    def remove_products_from_cart_by_category(self, request, cart_id):
        schema = RemoveProductsSchema(strict=True)

        try:
            category_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = RemoveProductsSchema().dump(category_data).data
        self.carts_rpc.remove_products_from_cart_by_category(
            cart_id,
            serialized_data['category_id'],
        )

        return 'success'

    @http("GET", "/search", expected_exceptions=(ValidationError, BadRequest))
    def search(self, request):
        schema = SearchSchema(strict=True)

        try:
            search_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = SearchSchema().dump(search_data).data
        result = self.search_rpc.search(
            serialized_data['user_id'],
            serialized_data['cart_items'],
        )
        logging.error(result)
        return f'{result}'
