#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-5
Email  : luffy.liu@maichuang.net
'''

# sys
#thirdparty
#self program
from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, DATETIME, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.models.base import BaseModel
from datetime import datetime


class Photos(BaseModel):
    __tablename__ = 'photos'

    id = Column('id', INTEGER, primary_key=True)
    hash_id = Column('hash_id', VARCHAR(128), nullable=False)
    file_name = Column('file_name', VARCHAR(128))
    size = Column('size', VARCHAR(64))
    image_info = Column('image_info', VARCHAR(256))
    tags = Column('tags', VARCHAR(256))
    remark = Column('remark', VARCHAR(1024))
    upload_time = Column('upload_time', DATETIME, default=datetime.now)
