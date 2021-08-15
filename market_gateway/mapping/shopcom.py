import logging
import random

class ShopcomMapping:

    def get_term_from_category(self, category):
        mapping = {
            'chocolate': 'chocolate',
            'salgadinho': 'chips',
            'leite condensado': 'condensed milk'
        }
        try:
            product = mapping[category]
        except KeyError: 
            product = random.choice(list(mapping.values()))
        return product
    
    def normalize_response(self, response):
        normalized = []
        for product in response:
            normalized.append({
                'name': product['name'],
                'price': product['minimumPrice'],
                'brand': product['brand']
            })
        return normalized