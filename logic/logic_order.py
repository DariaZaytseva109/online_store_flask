import uuid
from typing import List

from logic.logic_product import db


class Order:
    def __init__(self, product_ids: List[str], total=0, id=None):
        self.id = id
        self.product_ids = product_ids
        self.total = total


def create_order(id, product_ids):
    id = str(uuid.uuid4())
    total = 0
    for id in product_ids:
        pr = db.get_order(id)
        total += pr.price
    new_order = Order(id, product_ids, total)
    db.add_order(new_order)


def show_orders(page=0, limit=10):
    return db.list_orders(page=page, limit=limit)


def show_order(order_id):
    return db.get_order(order_id)


def update_order(order_id, product_ids: List[str]):
    total = 0
    for id in product_ids:
        pr = db.get_order(id)
        total += pr.price
    updated_order = Order(order_id, product_ids, total)
    db.change_order(updated_order)


def delete_order(order_id):
    db.del_order(order_id)
