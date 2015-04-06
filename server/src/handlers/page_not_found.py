#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-5
Email  : luffy.liu@maichuang.net
'''
from src.handlers.basic import BasicHandler

class PageNotFoundHandler(BasicHandler):
    """处理404页面"""

    def get(self, *args, **kwargs):
        self.set_status(404, 'Page Not Found')

    def post(self, *args, **kwargs):
        self.set_status(404, 'Page Not Found')

    def put(self, *args, **kwargs):
        self.set_status(404, 'Page Not Found')

    def delete(self, *args, **kwargs):
        self.set_status(404, 'Page Not Found')

    def patch(self, *args, **kwargs):
        self.set_status(404, 'Page Not Found')

    def options(self, *args, **kwargs):
        self.set_status(404, 'Page Not Found')