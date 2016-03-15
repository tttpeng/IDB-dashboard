from flask import Flask, render_template, request
import pymysql
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import request
from datetime import datetime
import  time
import hashlib
import base64
from Crypto import Random
from Crypto.Cipher import AES

import pyaes

app = Flask(__name__)
db = SQLAlchemy()







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
# # print (time.time())
# # NSString *encryptPassword = [[NSString stringWithFormat:@"%@:%lld", password, time] md5];
#


enc = 'Xu/FnoCtKClwIaJXWOgR9643PR3zMsGBDYuOung095c/2hZXgNVtwBY4RBiUlY0gbMfvs1DhignWEq+ayZYSQC7NzlQ9PaaYtegDqjadohGj1/N/TUhA5nH6zCchdo7A+GFsokA8pQKQIM7sH4SKHkqfkZAAAFQ7+Y3ZJp3xe+tGM132d6O3Q6r3S748nWfgbSDQC9Y/nQJI0tne1HRJ/XFaZpO3npNCf2shphXR06K31NgHVC0bnTdVNRGqTUBJbyvMGqOjKQgoBD6J5to/zusP3CnQX0ZjriawkQwOs9gURsMV8Gpmed9Zku/mkNV8R9P+C5CE3K0ue8v13mw65B2cLk/fJQ4ZoMMmVPQe37Yg8aoLBPuGqghtzFf/TbWQxPqjNNGp+qph9WKXiAm7xrNXMOCPkD9VlVN+lNidzDlJ0RWW95tLV+bQSiyk2j4cZzannlS3RKlxke/OVXJImpJxTuvC+X+YdTUu6G2Rneoy5C9o7dzifx7Gy6rgGpALiFb6ePltZWrZsdvktP2w2A8sl54Btjc+6LdCfj4kH+pd80DmIzCCwpMXe+AV/O7TyZTpJIDiCfT06D6nr5g0DPi6WE3rBGqo524zq9DLLESxQvP5oowpi43mZfM4wZvdhKFO9vQ7ZRiNSLmxsDhTXek7ZhjaIJrGFmXHMHBTBODlkxv4cPUzXhZWtDChQlqX2azIJyQiQMPebIao3Ltb63A3VWAirqGR3a2k/B4tXEmiDCID3PihgUXI3ZA3ONCtN1STzoIQu5gjjaIgxPS0n7w1FGWOcF3vTvnvQSG+ksle1X/YPCHidDoFgPo3L9XdB2xTAwxMGmsQLUUj8oJWC7dEuaK2+sZA3IvUvo4oN5ZJkArAIqCi2VOuIH/Yo5TGpND/JEFqpyB/KGzeJOe1GajW6MIXjcAdn91M8TAFPSvwJML9Cd2FTCqZocWbMDCV7SxHPqKplIjNPMIoV8BRQm4ApzojxeAzzzW9LMOfNGvcJwFJC/JLOzjqcweiNqiLG71jfyHNdOWmwZ57sW81zgxBK+jh0ZTeC+O7Bg5XS1s='
# iv = enc[:AES.block_size]
# cipher = AES.new('ihlih*0037JOHT*)(PIJY*(()JI^)IO%', AES.MODE_CBC, iv)
# one = cipher.decrypt(enc[AES.block_size:])
# two = one[:-ord(one[len(one)-1:])]
# three = two.decode()
#
# AESdecrypt(enc,'ihlih*0037JOHT*)(PIJY*(()JI^)IO%')


key = 'ihlih*0037JOHT*)(PIJY*(()JI^)IO%'


aes = pyaes.AESModeOfOperationCBC(bytes(key, encoding = "utf8")  )
print(base64.b64decode(enc))

# decrypted = aes.decrypt(base64.b64decode(enc))
# print(decrypted)
# print(decrypted.decode(encoding='gb2312'))
# print(str(decrypted, encoding = "gbk")  )

@app.route('/', methods=['GET', 'POST'])
def home():
    addData()
    print('There is none root.')
    return render_template("index.html",message='我的第一个jinja程序')
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


if __name__ == '__main__':
    app.run()

