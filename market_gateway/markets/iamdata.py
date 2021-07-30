import requests

class IAmData:
    name = 'iamdata'

    base_url = 'https://api.iamdata.co/v1'

    def search(self, term):
        upcs = self.get_products(term)
        self.get_prices(upcs)

    def get_products(self, term):
        response = requests.get(f'{self.base_url}/products')

    
    def get_prices(self, ids):
        response = requests.get(f'{self.base_url}/products_prices')