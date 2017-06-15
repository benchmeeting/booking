import json


class SimpleDict(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
