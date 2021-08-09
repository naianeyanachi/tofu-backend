from markets.grocerybear import GroceryBear


class Markets:
    markets = [
        GroceryBear()
    ]
    def search_all(self, categories):
        result = {}
        for market in self.markets:
            result[market.name] = {}
            for category in categories:
                result[market.name][category] = market.search(category)
        return result
                