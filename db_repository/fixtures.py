from app import db
from app.models import Item, Reservation
from copy import deepcopy
import datetime


db.create_all()

item = Item()
db.session.add(item)
db.session.add(deepcopy(item))
db.session.add(deepcopy(item))
db.session.commit()

res = Reservation(item_id=item.id,
                  date=datetime.datetime.now().date(),
                  start_time=datetime.datetime.now().time(),
                  duration=70)

db.session.add(res)
db.session.commit()
