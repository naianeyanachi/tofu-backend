import json
import logging

# from marshmallow import ValidationError
# from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy, rpc
from werkzeug import Response

# from gateway.exceptions import CartNotFound
# from gateway.schemas import (AddProductsSchema, CartSchema, CategorySchema,
#                              CreateCartSchema, ProductSchema, RemoveProductsSchema,
#                              SearchSchema)


class MarketGatewayService(object):
    """
    Service acts as a gateway to other services over http.
    """

    name = 'market_gateway'

    search_rpc = RpcProxy('search')

    @rpc
    def search(self):
        logging.error('aaaaa')
