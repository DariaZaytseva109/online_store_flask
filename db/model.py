class DBException(Exception):
    pass


class DB:
    def __init__(self):
        self.db_products = []
        self.db_orders = []

    def add_product(self, new_product):
        self.db_products.append(new_product)
        print('DB: Добавлен в базу', new_product.id)
        print(self.db_products)

    def change_product(self, new_product):
        self.db_products = [p for p in self.db_products if p.id != new_product.id]
        self.db_products.append(new_product)

    def get_product(self, product_id):
        return next((p for p in self.db_products if str(p.id) == str(product_id)), None)

    def list_products(self, page, limit):
        start = page * limit
        end = start + limit
        return self.db_products[start:end]

    def del_product(self, product_id):
        self.db_products = [p for p in self.db_products if p.id != product_id]
        print('DB: Удален из базы', product_id)

    def add_order(self, new_order):
        self.db_orders.append(new_order)
        print('DB: Добавлен в базу', new_order.id, "стоимость:", new_order.total)
        
    def change_order(self, new_order):
        self.db_orders = [o for o in self.db_products if o.id != new_order.id]
        self.db_orders.append(new_order)

    def get_order(self, order_id):
        return next((o for o in self.db_orders if o.id == order_id), None)

    def list_orders(self, page, limit):
        start = page * limit
        end = start + limit
        return self.db_orders[start:end]

    def del_order(self, order_id):
        self.db_orders = [o for o in self.db_orders if o.id != order_id]
        print('DB: Удален из базы', order_id)
