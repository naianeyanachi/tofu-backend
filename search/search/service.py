import logging

from nameko.events import EventDispatcher
from nameko.rpc import rpc

from search.exceptions import NotFound
from search.schemas import CartSchema


class SearchService:
    name = 'search'
    
    event_dispatcher = EventDispatcher()

    @rpc
    def search_by_cart(self, user_id, cart_id, cart_items):
        pass
