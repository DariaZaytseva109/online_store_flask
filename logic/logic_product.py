import uuid

from db.model import DB

db = DB()

class Product:
    def __init__(self, name: str, price: float, id=None):
        self.id = id
        self.name = name
        self.price = price


def create_product(name, price, id=None):
    if id is None:
        id = str(uuid.uuid4())
    new_product = Product(id=id, name=name, price=price)
    db.add_product(new_product)
    return new_product


def show_products(page=0, limit=10):
    return db.list_products(page=page, limit=limit)


def show_product(product_id):
    return db.get_product(product_id)


def delete_product(product_id):
    db.del_product(product_id)
