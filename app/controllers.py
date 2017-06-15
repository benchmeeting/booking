from app import application
from app.utils.representation import SimpleDict
from flask import request
from app.models import Item, Reservation
import json


@application.route("/", methods=['GET'])
@application.route("/fetch", methods=['GET'])
def get_all():
    items = Item.query.all() or []
    return json.dumps(items, cls=SimpleDict)


@application.route("/fetch/<int:id>", methods=['GET'])
def get_by_id(id):
    item = Item.query.filter_by(id=id)
    return item


@application.route("/create", methods=['POST'])
def create(request):
    return request.item_id


@application.route("/update", methods=['PUT', 'PATCH'])
def update(request):
    return -1


@application.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    return -1
