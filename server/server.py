#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-5
Email  : luffy.liu@maichuang.net
'''

import tornado.httpserver
import tornado.web
from src.settings import AK, SK
from tornado.options import options
from src.mappings import patterns
from tornado.httpserver import HTTPServer
from src.models.base import get_session
from tornado.log import access_log

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from tornado.options import parse_command_line
parse_command_line()


class App(tornado.web.Application):
    def __init__(self):
        super(App, self).__init__(patterns)

    @property
    def db_session(self):
        return get_session()

    @property
    def logger(self):
        return access_log

if __name__ == '__main__':
    if AK is None or SK is None:
        print u"当前AK和SK配置不正确，请在settings中修改"
        exit()

    options.parse_command_line()

    if options.initdb:
        from src.models import  *
        from src.models.base import init_db
        init_db()
        exit()

    http_server = HTTPServer(App())
    http_server.listen(options.port)
    io_loop = tornado.ioloop.IOLoop.instance()
    io_loop.start()
