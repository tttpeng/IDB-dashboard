from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


db = SQLAlchemy()

Base = declarative_base()

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Unicode(64), primary_key=True)
    name = db.Column(db.Unicode(64))
    host = db.Column(db.Unicode(64))
    is_operation = db.Column(db.Boolean)
    updateTime = db.Column(db.DateTime)

    @staticmethod
    def list_category():
        products = Product.query.all()
        return [c.to_json() for c in products]

    def to_json(self):
        if (self.is_operation):
            title = 'operation'
        else:
            title = 'fail'

        return {
            'name': self.name,
            'host': self.host,
            'is_operation': title,
            'updateTime': self.updateTime,
        }




