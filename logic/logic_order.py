import uuid
from typing import List

from logic.logic_product import db


class Order:
    def __init__(self, product_ids: List[str], total=0, id=None):
        self.id = id
        self.product_ids = product_ids
        self.total = total


def create_order(product_ids, id=None):
    if id is None:
        id = str(uuid.uuid4())
    total = 0
    for product_id in product_ids:
        pr = db.get_product(product_id)
        total += pr.price
    new_order = Order(id=id, product_ids=product_ids, total=total)
    db.add_order(new_order)
    return new_order


def show_orders(page=0, limit=10):
    return db.list_orders(page=page, limit=limit)


def show_order(order_id):
    return db.get_order(order_id)


def delete_order(order_id):
    db.del_order(order_id)
