import logging

from nameko.rpc import rpc

from markets.markets import Markets


class MarketGatewayService(object):
    name = 'market_gateway'

    markets = Markets()

    @rpc
    def search_by_categories(self, categories):
        return self.markets.search_all(categories)
