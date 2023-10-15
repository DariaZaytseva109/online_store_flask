from flask import Flask, request
from marshmallow import ValidationError

from logic.logic_order import create_order, show_order, show_orders
from logic.logic_product import show_product, show_products, create_product
from view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from view.product_schemas import ProductGetManyParams, ProductSchema, ProductCreateDtoSchema

app = Flask(__name__)


@app.get('/api/v1/product/<id>/')
def product_get_by_id_endpoint(id):
    product = show_product(id)
    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return ProductSchema().dump(product)


@app.get('/api/v1/product/')
def product_get_list_endpoint():
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    page = int(product_get_many_params["page"]) - 1
    limit = product_get_many_params["limit"]
    lst = show_products(page=page, limit=limit)
    return ProductSchema(many=True).dump(lst)


@app.post("/api/v1/product/")
def product_create_endpoint():
    try:
        product_get_params = ProductCreateDtoSchema().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    try:
        new_product = create_product(
            name=product_get_params["name"],
            price=product_get_params["price"],
            id=product_get_params.get("id"))
    except Exception as e:
        return {
            "error": str(e)
        }
    return ProductSchema().dump(new_product)


@app.post("/api/v1/order/")
def order_create_endpoint():
    print(request.is_json)
    print(request.json)
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = create_order(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order/")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = show_orders(
        page=order_get_many_params['page'] - 1,
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>/")
def order_get_by_id_endpoint(id):
    order = show_order(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)


def run_server():
    app.run()

