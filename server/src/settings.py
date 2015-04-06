#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-5
Email  : luffy.liu@maichuang.net
'''
from tornado.options import define

define('port', default=9999, type=int, help='Tornado will provide service on the given port')

#mysql setting
_db_config = {
    'db_type': 'mysql',
    'db_driven': 'mysqldb',
    'db_user': 'root',
    'db_passwd': 'bmw12345',
    'db_host': 'localhost',
    'db_port': '3306',
    'db_selected_db': 'photo_share',
    'db_charset': 'utf8'
}

_db_connect_params = '%(db_type)s+%(db_driven)s://%(db_user)s:%(db_passwd)s@%(db_host)s/%(db_selected_db)s?charset=%(db_charset)s'
DB_CONNECT_PARAMS = _db_connect_params % _db_config
DB_TIMEOUT = 3600


#qi niu setting
AK = 'EUh7eoMA83143fHa0k3hXp-KQn-2b_56B7uMNcQj'
SK = '2FKv6-X7IBRt-rp1_-j9n8N1VNXVn54dIL2DtNzN'

QINIU_DOMAIN = '7xidjv.com1.z0.glb.clouddn.com'
BUCKET_NAME = 'luffyliu'

UPLOAD_PYOLIC = {
    'callbackUrl': 'http://zanjia.ren/upload/callback',
    'callbackBody': 'filename=$(fname)&hash_id=$(key)&fsize=$(fsize)&imageInfo=$(imageInfo)'
}