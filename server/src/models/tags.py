#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-6
Email  : luffy.liu@maichuang.net
'''

from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, DATETIME, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.models.base import BaseModel
from datetime import datetime

class Tags(BaseModel):
    __tablename__ = 'tags'

    id = Column('id', INTEGER, primary_key=True)
    tag = Column('tag', VARCHAR(256))
    created = Column('created', DATETIME, default=datetime.now)

    @classmethod
    def add_tag(cls, tags):
        exist_tags = [t.tag for t in cls.objects.all()]

        for t in tags.split(','):
            if not t:
                continue
            if t not in exist_tags:
                tag = Tags()
                tag.tag = t
                tag.session.add(tag)