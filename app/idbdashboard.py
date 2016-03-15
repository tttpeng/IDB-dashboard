from flask import Flask, render_template, request
import pymysql
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import request
from datetime import datetime
import time
import hashlib
import os, sched


app = Flask(__name__)
db = SQLAlchemy()







# print (request.urlopen('https://www.douban.com/photos/album/1623990634/').read().decode('utf-8'))


def refresh():
    with request.urlopen('https://www.douban.com/photos/album/1623990634/') as f:
        data = f.read();
        print('Status:', f.status, f.reason)




s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    refresh()
    # do your stuff
    sc.enter(5, 1, do_something, (sc,))

s.enter(0, 1, do_something, (s,))
# s.run()



@app.route('/', methods=['GET', 'POST'])
def home():
    # addData()
    print('There is none root.')
    return render_template("index.html",message='This is IDB dashboard !!!')
    return 'Hello World!'

# db.init_app(app)
# db.app = app
# Base = declarative_base()
#
# # 定义User对象:
# class User(Base):
#     # 表的名字:
#     __tablename__ = 'user'
#
#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
#
#
#
#
# def addData():
#     engine = create_engine('mysql+pymysql://root:123@127.0.0.1:3306/test')
# # 创建DBSession类型:
#     DBSession = sessionmaker(bind=engine)
#
#     Base.metadata.create_all(engine)
#
#     db.create_all();
#
#     # 初始化数据库连接:
#     session = DBSession()
#     new_user = User(id='3',name='Pengtao')
#     session.add(new_user)
#     session.commit()
#     session.close()

# pymysql.connect
# def createdb():
#     connection = pymysql.connect(host='localhost',user = 'root', password='123',db='test')
#     try:
#         with connection.cursor() as cursor:
#             sql = 'CREATE TABLE Persons(Id_P int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))'
#             connection.cursor().execute(sql)
#             connection.commit()
#     finally:
#         connection.close()
#
#
#



# @app.route('/')
# def index():
#     return render_template('index.html', message)
# def index
#     username = request.form['username']
#     password = request.form['password']
#     if username=='admin' and password=='password':
#         return render_template('signin-ok.html', username=username)
#     return render_template('form.html', message='Bad username or password', username=username)


if __name__ == "__main__":
    app.run()

