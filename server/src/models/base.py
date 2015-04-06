#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-5
Email  : luffy.liu@maichuang.net
'''

from  datetime import datetime
# thirdparty
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from tornado.log import access_log
from src.settings import DB_CONNECT_PARAMS, DB_TIMEOUT

engine = create_engine(DB_CONNECT_PARAMS, echo=False, pool_recycle=DB_TIMEOUT)
BaseModel = declarative_base()


maker = sessionmaker(bind=engine)
DBSession = scoped_session(maker)

BaseModel.session = DBSession  # use the same session
BaseModel.objects = DBSession.query_property()  # get all objects

BaseModel.__table_args__ = {
    'mysql_charset': 'utf8',
    'mysql_engine': 'InnoDB'
}

def get_session():
    return DBSession

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)

def _json(self, spec=[], skip=[], date_format=None):
    data = {}
    for col in self.__table__.columns:
        if spec and str(col.name) not in spec:
            continue

        if skip and str(col.name) in skip:
            continue

        attr = getattr(self, col.name)
        if isinstance(attr, datetime):
            data[col.name] = attr.strftime(date_format or '%Y-%m-%d %H:%M:%S')
            continue

        data[col.name] = attr

    return data

def _anti_json(self, dicts, spec=[]):
    for key, val in dicts.items():
        if hasattr(self, key) and key in spec:
            setattr(self, key, val)
        else:
            access_log.warning(u'%s没有属性%s' % (self.__class__.__name__, key))



@classmethod
def find_one(cls, filter_dict):
    res = cls.objects
    for key, val in filter_dict.items():
        res = res.filter(getattr(cls, key) == val)

    return res.first()

@classmethod
def find_all(cls, filter_dict={}):
    res = cls.objects
    for key, val in filter_dict.items():
        res = res.filter(getattr(cls, key) == val)

    return res.all()


@classmethod
def get_lists(cls, filter_func=None):
    if filter_func is None:
        return [ins.json() for ins in cls.objects.all()]

    return [ins.json() for ins in cls.objects.all() if filter_func(ins)]


def _save(self):
    self.session.add(self)

def _delete(self):
    self.session.delete(self)

BaseModel.save = _save
BaseModel.delete = _delete
BaseModel.json = _json
BaseModel.find_one = find_one
BaseModel.find_all = find_all
BaseModel.get_lists = get_lists
BaseModel.anti_json = _anti_json

