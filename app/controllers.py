from app import application
from app.utils.representation import SimpleDict, DictOrDateTime
from flask import request, Response
from app.models import Item, Reservation
import json

response = Response(content_type='application/json; charset=utf-8')

@application.route("/", methods=['GET'])
@application.route("/fetch", methods=['GET'])
def get_all():
    items = Item.query.all() or []
    response.response = json.dumps(items, cls=DictOrDateTime)
    return response


@application.route("/fetch/<int:id>", methods=['GET'])
def get_by_id(id):
    item = Item.query.filter_by(id=id).first()
    response.response = json.dumps(item, cls=DictOrDateTime)
    return response


@application.route("/create", methods=['POST'])
def create(request):
    return request.item_id


@application.route("/update", methods=['PUT', 'PATCH'])
def update(request):
    return -1


@application.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    return -1
