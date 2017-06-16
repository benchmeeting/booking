from app import db
from sqlalchemy import Integer, Date, Time, Column, ForeignKey


class Item(db.Model):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    reservations = db.relationship('Reservation')

    # add your own columns/relationships here
    # ----

    def __getstate__(self):
        return {'id': self.id, 'reservations': [r.__getstate__() for r in self.reservations]}


class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    date = Column(Date, index=True)
    start_time = Column(Time)
    duration = Column(Integer)
    # add your own columns/relationships here
    # ----

    def __getstate__(self):
        """
        start_time format is hh:mm:ss
        duration in minutes
        :return: tuple
        """
        return {
                'id': self.id, 'item_id': self.item_id, 'date': self.date.isoformat(),
                'start_time': self.start_time.strftime('%X'), 'duration': self.duration
                }

# also you can add more models and relationships to build more complex business logic
# ----
