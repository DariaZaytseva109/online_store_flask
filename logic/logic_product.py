import uuid

from db.model import DB


db = DB()


class Product:
    def __init__(self, id: str, name: str, price: float):
        self.id = None
        self.name = name
        self.price = price


def create_product(name, price):
    id = str(uuid.uuid4())
    new_product = Product(id, name, price)
    db.add_product(new_product)


def show_all_products():
    return db.list_all_products


def show_product(product_id):
    return db.get_product(product_id)


def update_product(product_id, **kwargs):
    updated_product = Product(id=product_id, **kwargs)
    db.change_product(updated_product)


def delete_product(product_id):
    db.del_product(product_id)