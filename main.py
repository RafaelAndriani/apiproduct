from flask import Flask, request, Response
import service.clientservice as service
import json
from model.client import Client

app = Flask(__name__)


@app.get("/clients")
def clients():
    return Response(json.dumps(service.find_all(), default=lambda x: x.__dict__), mimetype="application/json")


@app.get("/clients/custom")
def custom():
    args = request.args
    column = args.get("column")
    value = args.get("value")
    return json.dumps(service.find_custom(column, value), default=lambda x: x.__dict__)


@app.post("/clients")
def save():
    data_json = request.json
    save_confirmation = service.save(Client(data_json["cnpj"], data_json["name"], data_json["address"]))
    if not save_confirmation:
        return Response("Invalid name", status=400, mimetype="application/json")
    return Response("Created", status=201, mimetype="application/json")


@app.delete("/clients")
def delete():
    data_json = request.json
    delete_ok = service.delete(data_json["cnpj"])
    if not delete_ok:
        return Response("Failed to delete", status=201, mimetype="application/json")
    return Response("Deleted", status=201, mimetype="application/json")


@app.post("/clients/update")
def update():
    data_json = request.json
    update_confirmation = service.update(Client(data_json["cnpj"], data_json["name"], data_json["address"]))
    if not update_confirmation:
        return Response("Invalid update", status=400, mimetype="application/json")
    return Response("Updated", status=201, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)
