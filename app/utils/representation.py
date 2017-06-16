import json


class SimpleDict(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class DictOrDateTime(json.JSONEncoder):
    def default(self, o):
        try:
            return o.__getstate__()
        except AttributeError:
            return o.__dict__
