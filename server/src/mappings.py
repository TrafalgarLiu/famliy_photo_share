#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-5
Email  : luffy.liu@maichuang.net
'''
from src.handlers.upload_token import UploadTokenHandler
from src.handlers.upload_callback import UploadCallback

from src.handlers.page_not_found import PageNotFoundHandler

ROOT = u''

patterns = [
    (ur'%s/upload/token/?' % ROOT, UploadTokenHandler),
    (ur'%s/upload/callback/?' % ROOT, UploadCallback),
    (ur'.*', PageNotFoundHandler),
]
