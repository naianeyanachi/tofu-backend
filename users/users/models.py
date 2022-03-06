import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )

DeclarativeBase = declarative_base(cls=Base)

class Address(DeclarativeBase):
    __tablename__ = "addresses"

    id = Column(String, primary_key=True)
    user_id = Column(
        String,
        ForeignKey("users.id", name="fk_user_id_addresses"),
        nullable=False
    )
    address = Column(String, nullable=False)
    number = Column(String, nullable=False)
    complement = Column(String, nullable=False)
    cep = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)


class User(DeclarativeBase):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    external_id = Column(String, nullable=False)
    authentication_id = Column(
        Integer,
        ForeignKey("authentication.id", name="fk_authentication_id_users"),
        nullable=False
    )
    pwd_hash = Column(String, nullable=False)
    pwd_salt = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)

    addresses = relationship("Address", cascade="delete")
