from flask import Flask

from logic.logic_product import show_product

app = Flask(__name__)




@app.get('/api/v1/product/<id>/')
def product_get_by_id_endpoint(id):
    product = show_product(id)

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return product


def run_server():
    app.run()

