import logging
import urllib

import requests

from mapping.shopcom import ShopcomMapping


class Shopcom:
    name = 'shop.com'

    base_url = 'https://api2.shop.com/AffiliatePublisherNetwork/v2'

    mapping = ShopcomMapping()

    headers = {
        'api_Key': '5d9d2b6cea7442538316e971ca45c5dd'
    }

    def search(self, category):
        term = self.mapping.get_term_from_category(category)
        products = self.get_products(term)
        return self.mapping.normalize_response(products)

    def get_site(self):
        response = requests.get(f'{self.base_url}/sites', headers=self.headers)
        return response.json()['sites'][0]

    def get_locale(self, site):
        response = requests.get(f'{self.base_url}/sites/{site}/locales', headers=self.headers)
        return response.json()['locales'][0]

    def get_products(self, term):
        params = {
            'publisherId': 'TEST',
            'categoryId': '1-32806',
            'locale': 'en_US',
            'site': 'shop',
            'term': term,
        }
        query_params = urllib.parse.urlencode(params)
        response = requests.get(f'{self.base_url}/products?{query_params}', headers=self.headers)
        return response.json()['products']
