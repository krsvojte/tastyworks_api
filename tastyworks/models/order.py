from enum import Enum


class OrderType(Enum):
    LIMIT = 'Limit'
    MARKET = 'Market'


class OrderEffect(Enum):
    CREDIT = 'Credit'
    DEBIT = 'Debit'

class OrderStatus(Enum):
    RECEIVED = 'Received'
    CANCELLED = 'Cancelled'
    FILLED = 'Filled'
    EXPIRED = 'Expired'


class Order(object):
    def __init__(self, type: OrderType, time_in_force: str, price: float, effect: OrderEffect):
        self.type = type
        self.time_in_force = time_in_force
        self.price = price
        self.effect = effect
