from flask import Flask, request
from marshmallow import ValidationError

from logic.logic_product import show_product, show_products, create_product
from view.product_schemas import ProductGetManyParams, ProductSchema, ProductCreateDtoSchema

app = Flask(__name__)


@app.get('/api/v1/product/<id>/')
def product_get_by_id_endpoint(id):
    print("PROCESS get_by_id")
    product = show_product(id)

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return ProductSchema().dump(product)


@app.get('/api/v1/product/')
def product_get_list_endpoint():
    print("PROCESS get_list")
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)
        print(request.args)
    except ValidationError as err:
        return err.messages, 400

    page = int(product_get_many_params["page"]) - 1
    limit = product_get_many_params["limit"]
    lst = show_products(page=page, limit=limit)
    return ProductSchema(many=True).dump(lst)


@app.post("/api/v1/product/")
def product_create_endpoint():
    print(request.args)
    try:
        product_get_params = ProductCreateDtoSchema().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    try:
        new_product = create_product(
            name=product_get_params["name"],
            price=product_get_params["price"],
            id=product_get_params.get("id"))
        print('Product created')
    except Exception as e:
        return {
            "error": str(e)
        }

    return ProductSchema().dump(new_product)



def run_server():
    app.run()

