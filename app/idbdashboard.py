from flask import Flask, render_template, request
from flask import render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.apscheduler import APScheduler
# from flask_apscheduler.scheduler import APScheduler
from sqlalchemy import Column, String,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from datetime import datetime
import time
import hashlib
import os, sched
import pymysql
from threading import Timer

from app import create_app
from app.models import Product
from app.models import db

import logging

from apscheduler.schedulers.background import BackgroundScheduler

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter(' %(pathname)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

#该代码片段来自于: http://www.sharejs.com/codes/python/6248


app = create_app()



    # 记录一条日志
logger.info('foorbar')


def job1(a, b):
    print(str(a) + ' ' + str(b))
def refresh():
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
    # 记录一条日志
    logger.info('foorbar')
    pp = Product.query.filter_by(name='WORKING_V2.0.0').first()
    if pp == None:
        pp = Product()
        pp.id = '2'
        pp.name = 'WORKING_V2.0.0'
    pp.is_operation = is_operation
    pp.updateTime = datetime.now()
    db.session.add(pp)
    db.session.commit()



@app.route('/', methods=['GET', 'POST'])
def home():
    logger.info('foorbar')
    print('There is none root.')
    return render_template("index.html",message='This is IDB dashboard !!!')

@app.route('/hello', methods=['GET', 'POST'])
def home2():
    logger.info('foorbar')
    return 'Hello World!'


@app.route('/products',methods=['GET'])
def list_product():
    print(Product.list_category())
    return jsonify(result=Product.list_category())




scheduler = BackgroundScheduler()
scheduler.add_job(refresh, 'interval', seconds=5)
scheduler.start()
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


