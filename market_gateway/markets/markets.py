from markets.grocerybear import GroceryBear
from markets.shopcom import Shopcom


class Markets:
    markets = [
        GroceryBear(),
        Shopcom(),
    ]

    def search_all(self, categories):
        result = {}
        for market in self.markets:
            result[market.name] = {}
            market_returned = False
            for category in categories:
                try:
                    result[market.name][category] = market.search(category)
                    market_returned = True
                except Exception:
                    pass
            if not market_returned:
                del result[market.name]
        return result
