from flask import Flask, render_template, request,jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import hashlib
import os, sched
import pymysql
from threading import Timer
import time

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
        logging.info(sss)
        dic = json.loads(sss)
        try:
            s = dic['Data']['User']
        except:
            storageWorking1(False)
        else:
            storageWorking1(True)
    else:
        storageWorking1(False)

def refreshWorking2():
    currentTime = int(time.time()) * 1000
    print(currentTime)
    password = '123:'+ str(currentTime)# print('没有加密的密码'+password)
    md5 = hashlib.md5(password.encode("utf-8"))
    encryptPassword = md5.hexdigest()
    url = 'http://dev.ideabinder.com/service/Login?appId=SFAWKCTR&username=LLB97483&password='+encryptPassword+'&appv=1.0.0605.1000&time='+str(currentTime)+'&tick=1458465920.940269'
    print(url)
    headers = {'Platform': '1'}
    r = requests.get(url,allow_redirects = False,headers = headers)
    if r.status_code == 200:
        ttt = r.text
        # sss = decrypt('ihlih*0037JOHT*)(PIJY*(()JI^)IO%',ttt)
        logging.info(ttt)
        dic = json.loads(ttt)
        try:
            s = dic['Data']['User']
        except:
            storageWorking2(False)
        else:
            storageWorking2(True)
    else:
        storageWorking2(False)

def refreshWorkingDSM():
    currentTime = int(time.time()) * 1000
    print(currentTime)
    password = '123:'+ str(currentTime)# print('没有加密的密码'+password)
    md5 = hashlib.md5(password.encode("utf-8"))
    encryptPassword = md5.hexdigest()
    url = 'https://www.sfaessentials.com/service/Login?appId=SFAWKCTD&username=Xdl12453&password='+encryptPassword+'&appv=1.0.0605.1000&time='+str(currentTime)+'&tick=1458709935.7343'
    print(url)
    headers = {'Platform': '1'}
    r = requests.get(url,allow_redirects = False,headers = headers)
    if r.status_code == 200:
        ttt = r.text
        sss = decrypt('ihlih*0037JOHT*)(PIJY*(()JI^)IO%',ttt)
        logging.info(sss)
        dic = json.loads(sss)
        print(dic)
        try:
            s = dic['Data']['User']
        except:
            storageWorkingDSM(False)
        else:
            storageWorkingDSM(True)
    else:
        storageWorkingDSM(False)


def refreshKnowledge():
    currentTime = int(time.time()) * 1000
    print(currentTime)
    password = '123:'+ str(currentTime)# print('没有加密的密码'+password)
    md5 = hashlib.md5(password.encode("utf-8"))
    encryptPassword = md5.hexdigest()
    url = 'http://dev.ideabinder.com/service/Login?appId=SFAWKCTR&username=Llb97483&password='+encryptPassword+'&tik=1458714486.077956&appv=1.0.0&time='+str(currentTime)
    print(url)
    r = requests.get(url,allow_redirects = False)
    if r.status_code == 200:
        ttt = r.text
        logging.info(ttt)
        dic = json.loads(ttt)
        try:
            s = dic['Data']['User']
        except:
            storageKnowledge(False)
        else:
            storageKnowledge(True)
    else:
        storageKnowledge(False)

def decrypt( key, enc ):
    enc2 = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(enc2)
    s = bytearray(decrypted)
    s = s.decode('utf-8').replace('\x00', '')
    return s


def unpad1(s):
    return s[:-ord(s[len(s)-1:])]

def storageWorking1(is_operation):
    pp = Product.query.filter_by(name='WORKING_V1.0.0').first()
    if pp == None:
        pp = Product()
        pp.id = '1'
        pp.name = 'WORKING_V1.0.0'
    pp.is_operation = is_operation
    pp.updateTime = datetime.now()
    db.session.add(pp)
    db.session.commit()

def storageWorking2(is_opertaion):
    pp = Product.query.filter_by(name='WORKING_V2.0.0').first()
    if pp == None:
        pp = Product()
        pp.id = '2'
        pp.name = 'WORKING_V2.0.0'
    pp.is_operation = is_opertaion
    pp.updateTime = datetime.now()
    db.session.add(pp)
    db.session.commit()

def storageWorkingDSM(is_opertaion):
    pp = Product.query.filter_by(name='WORKING_DSM_V1.0.0').first()
    if pp == None:
        pp = Product()
        pp.id = '3'
        pp.name = 'WORKING_DSM_V1.0.0'
    pp.is_operation = is_opertaion
    pp.updateTime = datetime.now()
    db.session.add(pp)
    db.session.commit()


def storageKnowledge(is_opertaion):
    pp = Product.query.filter_by(name='KNOWLEDGE_V1.1.0').first()
    if pp == None:
        pp = Product()
        pp.id = '4'
        pp.name = 'KNOWLEDGE_V1.1.0'
    pp.is_operation = is_opertaion
    pp.updateTime = datetime.now()
    db.session.add(pp)
    db.session.commit()



@app.route('/', methods=['GET', 'POST'])
def home():
    print('There is none root.')
    return render_template("index.html",message='This is IDB dashboard !!!')

@app.route('/hello', methods=['GET', 'POST'])
def home2():
    return 'Hello World!'


@app.route('/products',methods=['GET'])
def list_product():
    print(Product.list_category())
    return jsonify(result=Product.list_category())

@app.route('/allGroup.json',methods=['GET'])
def all():
    payload = {'uKey': '8f9d205b1aaee0ff18353cc091c4908d', '_api_key': 'ca1cbd6c6323f55e3d2364287dcd49e6'}
    r = requests.post('http://www.pgyer.com/apiv1/userAppGroup/listAll',data=payload)
    print(r.text)
    return r.text

@app.route('/allGroupApp.json',methods=['POST'])
def group():
    payload = {'userAppGroupKey': request.form['groupKey'], '_api_key': 'ca1cbd6c6323f55e3d2364287dcd49e6'}
    r = requests.post('http://www.pgyer.com/apiv1/userAppGroup/view',data=payload)
    print(r.text)
    return r.text







scheduler = BackgroundScheduler()
scheduler.add_job(refresh, 'interval', seconds=300)
scheduler.start()

scheduler2 = BackgroundScheduler()
scheduler2.add_job(refreshWorking2, 'interval', seconds=300)
scheduler2.start()

scheduler3 = BackgroundScheduler()
scheduler3.add_job(refreshWorkingDSM, 'interval', seconds=300)
scheduler3.start()

scheduler4 = BackgroundScheduler()
scheduler4.add_job(refreshKnowledge, 'interval', seconds=300)
scheduler4.start()

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


