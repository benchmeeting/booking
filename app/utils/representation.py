import json
import datetime
from sqlalchemy.orm.collections import InstrumentedList


class SimpleDict(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class DictOrDateTime(json.JSONEncoder):
    def default(self, o):
        try:
            return o.__dict__
        except AttributeError:
            if isinstance(o, datetime.date):
                return o.isoformat()
            else:
                return None