
class DBException(Exception):
    pass


class DB:
    def __init__(self):
        self.db_products = []
        self.db_orders = []

    def add_product(self, new_product):
        self.db_products.append(new_product)
        print('Добавлен')

    def change_product(self, new_product):
        self.db_products = [p for p in self.db_products if p.id != new_product.id]
        self.db_products.append(new_product)

    def get_product(self, product_id):
        try:
            return next(p for p in self.db_products if p.id == product_id)
        except Exception:
            return None

    def list_products(self, page, limit):
        start = page * limit
        end = start + limit
        return self.db_products[start:end]

    def del_product(self, product_id):
        self.get_product(product_id)
        self.db_products = [p for p in self.db_products if p.id != product_id]

    def add_order(self, new_order):
        self.db_orders.append(new_order)

    def change_order(self, new_order):
        self.db_orders = [o for o in self.db_products if o.id != new_order.id]
        self.db_orders.append(new_order)

    def get_order(self, order_id):
        try:
            return next(o for o in self.db_orders if o.id == order_id)
        except Exception:
            raise DBException(f"Order with id {order_id} doesn't exist")

    def list_orders(self, page, limit):
        start = page * limit
        end = start + limit
        return self.db_orders[start:end]

    def del_order(self, order_id):
        self.get_order(order_id)
        self.db_orders = [o for o in self.db_orders if o.id != order_id]

