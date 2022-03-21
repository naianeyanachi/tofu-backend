import logging

from nameko.rpc import RpcProxy, rpc
from nameko_sqlalchemy import DatabaseSession
from nanoid import generate

from search.exceptions import NotFound
from search.models import (Cart, CartItem, Category, DeclarativeBase,
                           MetadataField, MetadataValue, Product, Search)
from search.schemas import SearchSchema


class SearchService:
    name = 'search'

    market_gateway_rpc = RpcProxy('market_gateway')

    db = DatabaseSession(DeclarativeBase)

    def get_categories_and_cart(self, cart_id, user_id, cart_items):
        categories = set([])
        for i, cart_item in enumerate(cart_items):
            for j, value in enumerate(cart_item['product']['values']):
                cart_item['product']['values'][j] = MetadataValue(
                    id=value['id'],
                    value=value['value'],
                    field_id=value['field']['id'],
                    field=MetadataField(
                        id=value['field']['id'],
                        field=value['field']['field'],
                    ),
                )
            categories.add(cart_item['product']['category']['name'])
            cart_items[i] = CartItem(
                product_id=cart_item['product']['id'],
                id=generate(),
                quantity=cart_item['quantity'],
                cart_id=cart_id,
                product=Product(
                    id=cart_item['product']['id'],
                    category_id=cart_item['product']['category']['id'],
                    category=Category(
                       id=cart_item['product']['category']['id'],
                       name=cart_item['product']['category']['name'],
                    ),
                    values=cart_item['product']['values'],
                )
            )
        cart = Cart(
            id=cart_id,
            cart_items=cart_items,
            user_id=user_id
        )

        return list(categories), cart

    @rpc
    def search(self, user_id, cart_items):
        # add everything on search db
        #   don't add if already added

        cart_id = generate()
        categories, cart = self.get_categories_and_cart(cart_id, user_id, cart_items)
        self.db.merge(Search(
            id=generate(),
            cart_id=cart_id,
            cart=cart
        ))
        self.db.commit()

        # get user location and preferences
        #   get a list of matching supermarkets

        # search on each market on the list of supermarkets
        #   search products by category

        return self.market_gateway_rpc.search_by_categories(categories)

        # then filter results by metadata values
        #   make a buy list of each market

    @rpc
    def search_again(self, search_id):
        search = self.db.query(Search).get(search_id)

        if not search:
            raise NotFound('Search not found')

        search = SearchSchema().dump(search).data
        cart_id = search['cart']['id']
        user_id = search['cart']['user_id']
        cart_items = search['cart']['cart_items']
        new_search = Search(id=generate(), cart_id=cart_id)
        self.db.add(new_search)
        self.db.commit()

        categories, _ = self.get_categories_and_cart(cart_id, user_id, cart_items)
        return self.market_gateway_rpc.search_by_categories(categories)

    @rpc
    def get_search_history_by_user(self, user_id):
        searches = self.db.query(
            Search
        ).join(
            Search.cart
        ).filter(
            Cart.user_id == user_id
        ).order_by(
            Search.created_at.desc()
        ).all()
        return SearchSchema(many=True).dump(searches).data
