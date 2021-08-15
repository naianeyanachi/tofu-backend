import logging

from nameko.rpc import rpc, RpcProxy
from nameko_sqlalchemy import DatabaseSession
from nanoid import generate

from search.exceptions import NotFound
from search.schemas import SearchSchema, CartItemSchema, CartSchema
from search.models import DeclarativeBase, CartItem, Cart, Search, MetadataField, MetadataValue, Product, Category


class SearchService:
    name = 'search'

    market_gateway_rpc = RpcProxy('market_gateway')
    
    db = DatabaseSession(DeclarativeBase)

    @rpc
    def search(self, user_id, cart_items):
        # add everything on search db
        #   don't add if already added

        cart_id = generate()
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

        return self.market_gateway_rpc.search_by_categories(list(categories))

        # then filter results by metadata values
        #   make a buy list of each market


    @rpc
    def search_again(self, search_id):
        pass

    @rpc
    def get_search_history_by_user(self, user_id):
        searches = self.db.query(Search).join(Search.cart).filter(Cart.user_id == user_id).all()
        return SearchSchema(many=True).dump(searches).data
