import logging

import requests

from mapping.grocerybear import GroceryBearMapping


class GroceryBear:
    name = 'grocerybear'

    base_url = 'https://grocerybear.com/getitems'

    mapping = GroceryBearMapping()

    def search(self, category):
        headers = {
            'api-key': 'CFA327856422688ADCD11182479C8435E9FA54FE7034AE468B84CAB5172582EE'
        }
        data = {
            'product': self.mapping.get_product_from_category(category),
            'city': 'all',
            'num_days': 30
        }
        response = requests.post(self.base_url, data=data, headers=headers)
        return self.mapping.normalize_response(response.json())
