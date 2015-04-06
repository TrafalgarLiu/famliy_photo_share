#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-6
Email  : luffy.liu@maichuang.net
'''

import time
from qiniu import Auth
from hashlib import md5
from src.settings import AK, SK, BUCKET_NAME, UPLOAD_PYOLIC
from src.handlers.basic import BasicHandler
from src.models.photo import Photos

class UploadCallback(BasicHandler):

    def post_check(self):
        return True

    def post(self):
        if not self.post_check():
            return

        self.logger.info(self.request.query)
        self.logger.info('-------------------------')
        self.logger.info(self.request.query_arguments)
        self.logger.info('-------------------------')
        self.logger.info(self.request.body)
        self.logger.info('-------------------------')
        self.logger.info(self.request.body_arguments)
        self.return_json()