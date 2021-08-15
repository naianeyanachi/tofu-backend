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
            for category in categories:
                result[market.name][category] = market.search(category)
        return result
                