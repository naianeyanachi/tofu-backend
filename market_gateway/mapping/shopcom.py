import logging
import random

class ShopcomMapping:

    def get_term_from_category(self, category):
        mapping = {
            'ovos': 'eggs',
            'leite': 'milk',
            'pão': 'bread',
            'suco': 'juice',
            'arroz': 'rice',
            'carne': 'steak',
            'manteiga': 'butter',
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