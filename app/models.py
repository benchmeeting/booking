from app import db
from sqlalchemy import Integer, Date, Time, Column, ForeignKey


class Item(db.Model):
    id = Column(Integer, primary_key=True)
    reservations = db.relationship('Reservation', backref='item', lazy='joined')

    # add your own columns/relationships here
    # ----


class Reservation(db.Model):
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    date = Column(Date, index=True)
    start_time = Column(Time)
    duration = Column(Integer)
    # add your own columns/relationships here
    # ----


# also you can add more models and relationships to build more complex business logic
# ----
