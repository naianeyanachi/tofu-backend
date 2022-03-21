import logging

from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from nanoid import generate

from users.exceptions import NotFound
from users.models import Address, DeclarativeBase, User
from users.schemas import UserSchema


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
