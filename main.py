from flask import Flask, request, Response
import service.productservice as service
import json
from model.product import Product

app = Flask(__name__)


@app.get("/product")
def product():
    return Response(json.dumps(service.find_all(), default=lambda x: x.__dict__), mimetype="application/json")


@app.get("/product/custom")
def custom():
    args = request.args
    column = args.get("column")
    value = args.get("value")
    return json.dumps(service.find_custom(column, value), default=lambda x: x.__dict__)


@app.post("/product")
def save():
    data_json = request.json
    save_confirmation = service.save(Product(data_json["id"], data_json["name"], data_json["price"]))
    if not save_confirmation:
        return Response("Invalid save", status=400, mimetype="application/json")
    return Response("Created", status=201, mimetype="application/json")


@app.delete("/product")
def delete():
    data_json = request.json
    delete_ok = service.delete(data_json["id"])
    if not delete_ok:
        return Response("Failed to delete", status=400, mimetype="application/json")
    return Response("Deleted", status=200, mimetype="application/json")


@app.put("/product")
def update():
    data_json = request.json
    update_confirmation = service.update(Product(data_json["id"], data_json["name"], data_json["price"]))
    if not update_confirmation:
        return Response("Invalid update", status=400, mimetype="application/json")
    return Response("Updated", status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)
