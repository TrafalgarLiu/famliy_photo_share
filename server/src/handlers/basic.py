#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-5
Email  : luffy.liu@maichuang.net
'''
import json
import types
import urllib
import httplib
import tornado

from tornado.escape import json_encode


if type('') is not type(b''):
    def u(s):
        return s
    bytes_type = bytes
    unicode_type = str
    basestring_type = str
else:
    def u(s):
        return s.decode('unicode_escape')
    bytes_type = str
    unicode_type = unicode
    basestring_type = basestring

_TO_UNICODE_TYPES = (unicode_type, type(None))

def to_unicode(value):
     """Converts a string argument to a unicode string.

     If the argument is already a unicode string or None, it is returned
     unchanged.  Otherwise it must be a byte string and is decoded as utf8.
     """
     if isinstance(value, _TO_UNICODE_TYPES):
         return value
     if not isinstance(value, bytes_type):
         raise TypeError(
             "Expected bytes, unicode, or None; got %r" % type(value)
         )
     return value.decode("utf-8")

class BasicHandler(tornado.web.RequestHandler):

    def initialize(self, **kwargs):
        """
        初始化被__init__调用
        接受来自url_patterns中，第三个字典参数作为参数
        """
        pass

    def prepare(self):
        """
        该方法不能接受其他参数，否则报错
        用于数据库连接初始化等操作
        """
        self.parse_request_args()
        self.parse_request_body()
        pass

    def start_transaction(self):
        self.db_session.begin_nested()

    def end_transaction(self):
        self.db_session.commit()

    @property
    def logger(self):
        return self.application.logger

    @property
    def db_session(self):
        return self.application.db_session

    def get(self, *args, **kwargs):
        self.set_status(405, 'Method Not Allowed')

    def post(self, *args, **kwargs):
        self.set_status(405, 'Method Not Allowed')

    def put(self, *args, **kwargs):
        self.set_status(405, 'Method Not Allowed')

    def delete(self, *args, **kwargs):
        self.set_status(405, 'Method Not Allowed')

    def patch(self, *args, **kwargs):
        self.set_status(405, 'Method Not Allowed')

    def options(self, *args, **kwargs):
        """
        处理CORS Preflighted request
        默认由set_default_headers完成
        """
        pass

    def on_finish(self):
        """
        RequestHandler最后执行的方法，被finish()调用
        释放资源等操作在这里完成
        """
        self.db_session.close()
        pass

    def return_json(self, status_code=200, reason=None, data={}):
        """
        返回json数据，如果有callback则返回jsonp
        """
        assert isinstance(data, (types.BooleanType,
                                 types.NoneType,
                                 types.StringType,
                                 types.DictType,
                                 types.ListType,
                                 types.StringTypes))
        if reason is None:
            reason = httplib.responses.get(status_code)

        callback = self.get_argument('callback', '') or self.get_argument('jsonp', '')
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.set_status(status_code, reason)

        if data is not None:
            json_data = json_encode(data)
            data_p = callback + '(' + json_data + ')' if callback else json_data
            self.request_result = data_p
            self.write(data_p)


    def set_default_headers(self):
        """
        RequestHandler基类初始化时执行该方法
        设置默认响应header
        post, get, put, delete, patch, options都会执行该方法
        """
        self.set_access_control_header()

    def set_access_control_header(self):
        """
        用于和options方法协商
        跨域Access-Control头信息
        """
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'Content-Type, Depth, User-Agent, '
                        'X-File-Size, X-Requested-With, '
                        'X-Requested-By, If-Modified-Since, '
                        'X-File-Name, Cache-Control,'
                        'Authorization, X-Testing, Tan14-Key, User-Id, '
                        'Accept, Accept-Encoding, Accept-Language, Referer, Host, Origin')

    def parse_request_args(self):
        '''
            处理QueryString
            因没有标准来处理相同的字段
            这里采用若有相同的字段则取最后一个值
        '''
        if hasattr(self, '_request_args'):
            return getattr(self, '_request_args')
        data = {}
        for key, val in self.request.query_arguments.items():
            if not val:
                continue
            data[ key] = to_unicode(val[-1])

        setattr(self, '_request_args', data)
        return data

    def parse_request_body(self):
        """ 处理application/json类型的请求 """
        if hasattr(self, '_request_body'):
            return getattr(self, '_request_body')
        body = {}
        if self.request.body:
            try:
                body = json.loads(self.request.body)
            except ValueError:
                #TODO: 要先转译 不然因为split('&')的分隔字符是unicode对象
                #TODO：会导致split出来的也是unicode对象，且值是未转译的所以会乱码
                unquote_body = urllib.unquote_plus(self.request.body)
                tmp = unquote_body.split('&')
                try:
                    for item in tmp:
                        r = item.split('=')
                        if len(r) != 2:
                            continue
                        k, v = r

                        body[k.strip()] = v.strip()
                except ValueError as e:
                    pass
        setattr(self, '_request_body', body)
        return body