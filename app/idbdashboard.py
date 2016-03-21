from flask import Flask, render_template, request
from flask import render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from datetime import datetime
import hashlib
import os, sched
import pymysql
from threading import Timer
import time
import re

from app import create_app
from app.models import Product
from app.models import db
import logging
import requests
import base64
from Crypto.Cipher import AES
import json

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





# print (request.urlopen('https://www.douban.com/photos/album/1623990634/').read().decode('utf-8'))


# time = int(time.time()) * 1000
#
#
# password = '123:'+ str(time)# print('没有加密的密码'+password)
# md5 = hashlib.md5('123:1458032950377'.encode("utf-8"))
# encryptPassword = md5.hexdigest()
#
# print('加密之后的密码'+md5.hexdigest())
# print(time)
# # NSString *encryptPassword = [[NSString stringWithFormat:@"%@:%lld", password, time] md5];
#


def job1(a, b):
    print(str(a) + ' ' + str(b))
def refresh():
    currentTime = int(time.time()) * 1000
    print(currentTime)
    password = '123:'+ str(currentTime)# print('没有加密的密码'+password)
    md5 = hashlib.md5(password.encode("utf-8"))
    encryptPassword = md5.hexdigest()
    url = 'https://www.sfaessentials.com/service/Login?appId=SFAWKCTR&username=JJz83571&password='+encryptPassword+'&appv=1.0.0605.1000&time='+str(currentTime)+'&tick=1458465920.940269'
    print(url)
    headers = {'Platform': '1'}
    r = requests.get(url,allow_redirects = False,headers = headers)
    if r.status_code == 200:
        ttt = r.text
        sss = decrypt('ihlih*0037JOHT*)(PIJY*(()JI^)IO%',ttt)
        dic = json.loads(sss)
        if len(dic['Data']['User']) > 0:
            storageWorking1(True)
        else:
            storageWorking1(False)
        storageWorking1(True)
    else:
        storageWorking1(False)





def decrypt( key, enc ):
    enc2 = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(enc2)
    s = bytearray(decrypted)
    return s[:-11].decode('utf-8')



def unpad1(s):
    return s[:-ord(s[len(s)-1:])]

    # try:
    #     response = urlopen(req)
    # except HTTPError as e:
    #     print('The server couldnt fulfill the request.')
    #     print('Error code: ', e.code)
    #     storageWorking1(False)
    # except URLError as e:
    #     print('We failed to reach a server.')
    #     print('Reason: ', e.reason)
    #     storageWorking1(False)
    # else:
    #     print(response.status)
    #     if response.status == 200:
    #         storageWorking1(True)
    #     else:
    #         storageWorking1(False)
    #     print("good!")
    #     print(response.read().decode("utf8"))

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
scheduler.add_job(refresh, 'interval', seconds=3)
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


