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





