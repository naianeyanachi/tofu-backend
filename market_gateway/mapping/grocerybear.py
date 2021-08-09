import logging
import random

class GroceryBearMapping:

    def get_product_from_category(self, category):
        # eggs, milk, bread, orange juice (oj), rice, steak, or butter
        mapping = {
            'ovo': 'eggs',
            'leite': 'milk',
            'pão': 'bread',
            'suco': 'orange juice (oj)',
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
        normalized = {}
        for obj in response:
            city = obj['city']
            product_name = obj['title']
            price = obj['price']
            if city not in normalized:
                normalized[city] = []
            index = next(
                (i for i, item in enumerate(normalized[city]) if item['name'] == product_name),
                None
            )
            if index is not None:
                normalized[city][index]['price'] = min(price, normalized[city][index]['price'])
            else:
                normalized[city].append({
                    'name': product_name,
                    'price': price
                })
        logging.error(normalized)
        return normalized