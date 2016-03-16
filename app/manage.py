#!/usr/bin/env python
# coding: utf-8
from flask.ext.script import Manager
from app import create_app
from models import db
from werkzeug.security import generate_password_hash



manager = Manager(app)


@manager.command
def create_db():
    """Create database for """
    db.create_all()


# @manager.option('-u', '--name', dest='name', default='admin')
# @manager.option('-p', '--password', dest='password', default='123456')
# def create_user(name, password):
#     admin = User(name, generate_password_hash(password))
#     db.session.add(admin)
#     db.session.commit()


if __name__ == '__main__':
    manager.run()