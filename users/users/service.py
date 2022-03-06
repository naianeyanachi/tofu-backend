import logging

from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from nanoid import generate

from users.exceptions import NotFound
from users.models import DeclarativeBase, User, Address
from users.schemas import UserSchema, AddressSchema


class UsersService:
    name = 'users'

    db = DatabaseSession(DeclarativeBase)

    @rpc
    def get_user(self, user_id):
        user = self.db.query(User).get(user_id)

        if not user:
            raise NotFound('User not found')

        return UserSchema().dump(user).data

    @rpc
    def create_user_by_password(self, user):
        user_id = generate()
        user = User(
            id=user_id,
            authentication_id=1,
            pwd_hash=user['pwd_hash'],
            pwd_salt=user['pwd_salt'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            email=user['email'],
            phone=user['phone']
        )

        self.db.add(user)
        self.db.commit()

        return {
            'id': user_id
        }

    @rpc
    def create_address(self, user_id, address):
        address_id = generate()
        address = Address(
            id=generate(),
            user_id=user_id,
            address=address['address'],
            number=address['number'],
            complement=address['complement'],
            cep=address['cep'],
            city=address['city'],
            state=address['state']
        )

        self.db.add(address)
        self.db.commit()

        return {
            'id': address_id
        }


    # @rpc
    # def add_products_to_cart(self, cart_id, category_id, product_ids, quantity):
    #     self.remove_products_from_cart_by_category(cart_id, category_id)
    #     cart_items = [
    #         CartItem(
    #             id=generate(),
    #             cart_id=cart_id,
    #             product_id=product_id['product_id'],
    #             quantity=quantity
    #         )
    #         for product_id in product_ids
    #     ]
    #     for cart_item in cart_items:
    #         self.db.add(cart_item)
    #     self.db.commit()

    #     cart_items = CartItemSchema(many=True).dump(cart_items).data

    # @rpc
    # def remove_products_from_cart_by_category(self, cart_id, category_id):
    #     cart_items = self.db.query(CartItem).join(CartItem.product).filter(CartItem.cart_id == cart_id).filter(Product.category_id == category_id).all()
    #     for cart_item in cart_items:
    #         self.db.delete(cart_item)
    #     self.db.commit()

    # @rpc
    # def remove_all_products_from_cart(self, cart_id):
    #     cart_items = self.db.query(CartItem).join(CartItem.product).filter(CartItem.cart_id == cart_id).all()
    #     for cart_item in cart_items:
    #         self.db.delete(cart_item)
    #     self.db.commit()

    # @rpc
    # def get_categories_by_term(self, term):
    #     categories = self.db.query(Category).filter(Category.name.like(f'%{term}%')).all()

    #     if not categories:
    #         raise NotFound('Category not found')

    #     return CategorySchema(many=True).dump(categories).data

    # @rpc
    # def get_products_by_category(self, category_id):
    #     products = self.db.query(Product).filter(Product.category_id == category_id).all()

    #     if not products:
    #         raise NotFound(f'Product not found')

    #     return ProductSchema(many=True).dump(products).data

    # @rpc
    # def rename_cart(self, cart_id, name):
    #     cart = self.db.query(Cart).get(cart_id)
    #     cart.name = name
    #     self.db.commit()

    # @rpc
    # def delete_cart(self, cart_id):
    #     cart = self.db.query(Cart).get(cart_id)
    #     self.db.delete(cart)
    #     self.db.commit()

    # @rpc
    # def get_carts_by_user(self, user_id):
    #     carts = self.db.query(Cart).filter(Cart.user_id == user_id).all()

    #     if not carts:
    #         raise NotFound('User not found')

    #     return CartSchema(many=True).dump(carts).data
