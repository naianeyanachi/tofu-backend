from nameko.events import EventDispatcher
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession

from carts.exceptions import NotFound
from carts.models import DeclarativeBase, Cart, Category, Products, CartItem, MetadataField, MetadataValue
from carts.schemas import CartSchema, CartsCollectionSchema, CategoryCollectionSchema, ProductCollectionSchema

import logging


class CartsService:
    name = 'carts'

    db = DatabaseSession(DeclarativeBase)
    event_dispatcher = EventDispatcher()

    @rpc
    def get_cart(self, cart_id):
        cart = self.db.query(Cart).get(cart_id)

        if not cart:
            raise NotFound(f'Cart not found')

        return CartSchema().dump(cart).data

    @rpc
    def add_products_to_cart(self, cart_id, product_ids, quantity):
        cart = Cart(
            cart_id=cart_id,
            cart_items=[
                CartItem(
                    cart_id=cart_id,
                    product_id=product_id,
                    quantity=quantity
                )
                for product_id in product_ids
            ]
        )
        self.db.add(cart)
        self.db.commit()

        cart = CartSchema().dump(cart).data

        self.event_dispatcher('products_added', {
            'cart_id': cart_id,
            'cart_items': cart.cart_items,
        })

        return cart

    @rpc
    def remove_products_from_cart(self, cart_id, products, quantity):
        pass

    @rpc
    def remove_all_products_from_cart(self, cart_id):
        pass

    @rpc
    def get_categories_by_term(self, term):
        categories = self.db.query(Category).get(term)

        if not categories:
            raise NotFound(f'Category not found')

        return CategoryCollectionSchema().dump(categories).data

    @rpc
    def get_products_by_category(self, category_id):
        products = self.db.query(Products).get(category_id)

        if not products:
            raise NotFound(f'Product not found')

        return ProductCollectionSchema().dump(products).data

    @rpc
    def delete_cart(self, cart_id):
        pass

    @rpc
    def create_cart(self, cart_id, user_id):
        cart = Cart(cart_id=cart_id, user_id=user_id)

        self.db.add(cart)
        self.db.commit()

        cart = CartSchema().dump(cart).data

        self.event_dispatcher('products_added', {
            'cart': cart,
        })

        pass

    @rpc
    def get_carts_by_user(self, user_id):
        carts = self.db.query(Cart).get(user_id)

        if not carts:
            raise NotFound(f'User not found')

        return CartsCollectionSchema().dump(carts).data
    #------------------------------------------------------------------
    # @rpc
    # def update_order(self, order):
    #     order_details = {
    #         order_details['id']: order_details
    #         for order_details in order['order_details']
    #     }

    #     order = self.db.query(Order).get(order['id'])

    #     for order_detail in order.order_details:
    #         order_detail.price = order_details[order_detail.id]['price']
    #         order_detail.quantity = order_details[order_detail.id]['quantity']

    #     self.db.commit()
    #     return OrderSchema().dump(order).data

    # @rpc
    # def delete_order(self, order_id):
    #     order = self.db.query(Order).get(order_id)
    #     self.db.delete(order)
    #     self.db.commit()
