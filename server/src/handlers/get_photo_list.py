#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-6
Email  : luffy.liu@maichuang.net
'''


from src.handlers.basic import BasicHandler
from src.models.photo import Photos

class GetPhotoListHandler(BasicHandler):

    def check_get(self):
        return True

    def get(self):
        if not self.check_get():
            return

        tags = self._request_args.get('tags', None)
        self.return_json(data=Photos.get_phots_url(tags=tags))