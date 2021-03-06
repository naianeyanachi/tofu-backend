import json
import logging

from marshmallow import ValidationError
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from gateway.entrypoints import http
from gateway.exceptions import CartNotFound
from gateway.schemas import (AddProductsSchema, CartSchema, CategorySchema,
                             CreateAddressSchema, CreateCartSchema,
                             CreatePasswordUserSchema, ProductSchema,
                             RemoveProductsSchema, RenameCartSchema,
                             SearchHistorySchema, SearchSchema, UserSchema)


class GatewayService(object):
    name = 'gateway'

    carts_rpc = RpcProxy('carts')
    search_rpc = RpcProxy('search')
    users_rpc = RpcProxy('users')

    # CARTS SERVICE ------------------------------------------------------------------------

    @http("GET", "/cart/<string:cart_id>", expected_exceptions=CartNotFound)
    def get_cart(self, _, cart_id):
        cart = self.carts_rpc.get_cart(cart_id)
        return Response(
            CartSchema().dumps(cart).data,
            mimetype='application/json'
        )

    @http("GET", "/user/<string:user_id>/carts", expected_exceptions=CartNotFound)
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

    @http("GET", "/sector/<string:sector_id>/products", expected_exceptions=CartNotFound)
    def get_products_by_sector(self, _, sector_id):
        product_collection = self.carts_rpc.get_products_by_sector(sector_id)
        return Response(
            ProductSchema(many=True).dumps(product_collection).data,
            mimetype='application/json'
        )

    @http("GET", "/department/<string:department_id>/products", expected_exceptions=CartNotFound)
    def get_products_by_department(self, _, department_id):
        product_collection = self.carts_rpc.get_products_by_department(department_id)
        return Response(
            ProductSchema(many=True).dumps(product_collection).data,
            mimetype='application/json'
        )

    @http("GET", "/sector/<string:sector_id>/categories", expected_exceptions=CartNotFound)
    def get_categories_by_sector(self, _, sector_id):
        categories = self.carts_rpc.get_categories_by_sector(sector_id)
        return Response(
            CategorySchema(many=True).dumps(categories).data,
            mimetype='application/json'
        )

    @http("GET", "/department/<string:department_id>/categories", expected_exceptions=CartNotFound)
    def get_categories_by_department(self, _, department_id):
        categories = self.carts_rpc.get_categories_by_department(department_id)
        return Response(
            CategorySchema(many=True).dumps(categories).data,
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
            serialized_data['user_id'],
            serialized_data['name']
        )
        return Response(
            json.dumps({'id': result['id']}),
            mimetype='application/json'
        )

    @http("POST", "/cart/<string:cart_id>/products", expected_exceptions=(BadRequest))
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

    @http("PUT", "/cart/<string:cart_id>", expected_exceptions=CartNotFound)
    def rename_cart(self, request, cart_id):
        schema = RenameCartSchema(strict=True)

        try:
            name_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = RenameCartSchema().dump(name_data).data
        self.carts_rpc.rename_cart(
            cart_id,
            serialized_data['name']
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

    # SEARCH SERVICE ------------------------------------------------------------------------

    @http("POST", "/search", expected_exceptions=(ValidationError, BadRequest))
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
        return Response(
            json.dumps(result),
            mimetype='application/json'
        )

    @http("POST", "/search/<string:search_id>")
    def search_again(self, _, search_id):
        result = self.search_rpc.search_again(search_id)
        return Response(
            json.dumps(result),
            mimetype='application/json'
        )

    @http("GET", "/user/<string:user_id>/history")
    def get_search_history_by_user(self, _, user_id):
        searches = self.search_rpc.get_search_history_by_user(user_id)
        return Response(
            SearchHistorySchema(many=True).dumps(searches).data,
            mimetype='application/json'
        )

    # USERS SERVICE -------------------------------------------------------------------------

    @http("POST", "/user")
    def create_user_by_password(self, request):
        schema = CreatePasswordUserSchema(strict=True)

        try:
            user_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = CreatePasswordUserSchema().dump(user_data).data
        result = self.users_rpc.create_user_by_password(
            serialized_data
        )
        return Response(
            json.dumps(result),
            mimetype='application/json'
        )

    @http("POST", "/user/<string:user_id>/address")
    def create_address(self, request, user_id):
        schema = CreateAddressSchema(strict=True)

        try:
            address_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = CreateAddressSchema().dump(address_data).data
        result = self.users_rpc.create_address(
            user_id,
            serialized_data
        )
        return Response(
            json.dumps(result),
            mimetype='application/json'
        )

    @http("GET", "/user/<string:user_id>")
    def get_user(self, _, user_id):
        result = self.users_rpc.get_user(user_id)
        return Response(
            UserSchema().dumps(result).data,
            mimetype='application/json'
        )
