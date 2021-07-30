import logging

from nameko.rpc import rpc, RpcProxy

from search.exceptions import NotFound
from search.schemas import CartSchema


class SearchService:
    name = 'search'

    market_gateway_rpc = RpcProxy('market_gateway')

    @rpc
    def search(self, user_id, cart_items):
        # add everything on search db
        #   don't add if already added
        # get user location and preferences
        #   get a list of matching supermarkets
        # search on each market on the list of supermarkets
        #   search products by category
        #   then filter results by metadata values
        #   make a buy list of each market
        # return
        self.market_gateway_rpc.search()
        pass

    @rpc
    def search_again(self, search_id):
        pass

    @rpc
    def get_search_history_by_user(self, user_id):
        pass
