import logging

from nameko.events import EventDispatcher
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from nanoid import generate

from carts.exceptions import NotFound
from carts.models import (Cart, CartItem, Category, DeclarativeBase,
                          MetadataField, MetadataValue, Product)
from carts.schemas import CartSchema, CategorySchema, ProductSchema


class CartsService:
    name = 'carts'

    db = DatabaseSession(DeclarativeBase)
    event_dispatcher = EventDispatcher()

    @rpc
    def get_cart(self, cart_id):  # OK
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
    def remove_products_from_cart(self, cart_id, products, quantity):  # TODO
        pass

    @rpc
    def remove_all_products_from_cart(self, cart_id):  # TODO
        pass

    @rpc
    def get_categories_by_term(self, term):  # OK
        categories = self.db.query(Category).filter(Category.name.like(f'%{term}%')).all()

        if not categories:
            raise NotFound(f'Category not found')

        return CategorySchema(many=True).dump(categories).data

    @rpc
    def get_products_by_category(self, category_id):  # OK
        products = self.db.query(Product).join(Product.values).join(MetadataValue.field).filter(Product.category_id == category_id).all()

        if not products:
            raise NotFound(f'Product not found')

        return ProductSchema(many=True).dump(products).data

    @rpc
    def delete_cart(self, cart_id):  # TODO
        pass

    @rpc
    def create_cart(self, user_id):  # OK
        cart = Cart(id=generate(), user_id=user_id)

        self.db.add(cart)
        self.db.commit()

        cart = CartSchema().dump(cart).data

        self.event_dispatcher('products_added', {
            'cart': cart,
        })

        return cart

    @rpc
    def get_carts_by_user(self, user_id):  # OK
        carts = self.db.query(Cart).filter(Cart.user_id == user_id).all()

        if not carts:
            raise NotFound(f'User not found')

        return CartSchema(many=True).dump(carts).data

    # ------------------------------------------------------------------
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
