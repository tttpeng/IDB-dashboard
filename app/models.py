from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime


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
            'updateTime': pretty_date(self.updateTime),
        }


#http://stackoverflow.com/questions/1551382/user-friendly-time-format-in-python
def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "刚刚"
        if second_diff < 60:
            return str(second_diff) + " 秒前"
        if second_diff < 120:
            return "1分钟前"
        if second_diff < 3600:
            return str(int(second_diff / 60)) + " 分钟前"
        if second_diff < 7200:
            return "1小时前"
        if second_diff < 86400:
            return str(second_diff / 3600) + " 小时前"
    if day_diff == 1:
        return "去年"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"