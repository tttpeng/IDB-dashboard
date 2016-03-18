from flask import Flask, render_template, request
import pymysql
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import request
import urllib.request
from datetime import datetime
import time
import hashlib
import os, sched
from models import Product
from app import models
from flask.ext.sqlalchemy import SQLAlchemy
from models import db
# from app import create_app
from __init__ import create_app

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from flask import render_template, request, jsonify
from flask import jsonify

app = create_app()

import time
from threading import Timer
#
# def print_time( enter_time ):
#     print ("now is", time.time() , "enter_the_box_time is", enter_time)
#
#
# print (time.time())
# Timer(5,  print_time, ( time.time(), )).start()
# Timer(10, print_time, ( time.time(), )).start()
# print (time.time())
#
#
#
# new_prodcut = Product()
# new_prodcut.id  = 1;
# new_prodcut.name = '哈哈你猜'
# print(new_prodcut.name)
#

# print (request.urlopen('https://www.douban.com/photos/album/1623990634/').read().decode('utf-8'))


from flask_apscheduler import APScheduler


class Config(object):
    JOBS = [
        {
            'id': 'refresh',
            'func': '__main__:refresh',
            'args': (1,2),
            'trigger': 'interval',
            'seconds': 3
        }
    ]

    SCHEDULER_VIEWS_ENABLED = True


def job1(a, b):
    print(str(a) + ' ' + str(b))
def refresh(a,b):
    req = Request("http://www.v2ex.com/")
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldnt fulfill the request.')
        print('Error code: ', e.code)
        storageWorking1(False)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        storageWorking1(False)
    else:
        print(response.status)
        if response.status == 200:
            storageWorking1(True)
        else:
            storageWorking1(False)
        print("good!")
        # print(response.read().decode("utf8"))


def storageWorking1(is_operation):
    pp = Product.query.filter_by(name='WORKING_V2.0.0').first()
    if pp == None:
        pp = Product()
        pp.id = '2'
        pp.name = 'WORKING_V2.0.0'
    pp.is_operation = is_operation
    pp.updateTime = datetime.now()
    db.session.add(pp)
    db.session.commit()


#
# app.config.from_object(Config())
#
# scheduler = APScheduler()
# scheduler.init_app(app)
# scheduler.start()

#------

def task(func, interval, delay):
    start = time.time()
    if delay != 0:
        sleep(delay)
    func()
    end = time.time()
    if start + interval > end:
        Timer(start + interval - end, task, (func, interval, 0)).start()
    else:
        times = round(end - start / interval)  # times >= 1
        Timer(start + (times + 1) * interval - end, task, (func, interval, 0)).start()


def scheduler(func, interval, delay=0):
    Timer(interval, task, (func, interval, delay)).start()

def say_hello():
    # sleep(0.7)
    print(str(time.time()) + ' : hello')
# scheduler(say_hello, 1, 0)





# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     refresh()
#     # do your stuff
#     sc.enter(5, 1, do_something, (sc,))


@app.route('/', methods=['GET', 'POST'])
def home():
    # addData()
    print('There is none root.')
    return render_template("index.html",message='This is IDB dashboard !!!')

@app.route('/hello', methods=['GET', 'POST'])
def home2():
    return 'Hello World!'


@app.route('/products',methods=['GET'])
def list_product():
    print(Product.list_category())
    return jsonify(result=Product.list_category())

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

