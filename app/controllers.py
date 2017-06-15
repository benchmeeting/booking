from app import application
from app.utils.representation import SimpleDict
from flask import request
import json


@application.route("/", methods=['GET'])
@application.route("/fetch", methods=['GET'])
def get_all():
    items = []

    return json.dumps(items, cls=SimpleDict)


@application.route("/fetch/<int:id>", methods=['GET'])
def get_by_id(id):
    return -1


@application.route("/create", methods=['POST'])
def create(request):
    return -1


@application.route("/update", methods=['PUT', 'PATCH'])
def update(request):
    return -1


@application.route("/delete/<int:id>", methods=['DELETE'])
def update(id):
    return -1
