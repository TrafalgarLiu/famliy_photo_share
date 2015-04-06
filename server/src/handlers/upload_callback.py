#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-6
Email  : luffy.liu@maichuang.net
'''

from src.handlers.basic import BasicHandler
from src.models.photo import Photos
from src.models.tags import Tags

class UploadCallback(BasicHandler):

    def post_check(self):
        return True

    def post(self):
        if not self.post_check():
            return

        self.start_transaction()
        try:
            photo = Photos()
            photo.filename = self._request_body['filename']
            photo.size = self._request_body['fsize']
            photo.image_info = self._request_body['imageInfo']
            photo.hash_id = self._request_body['hash_id']
            photo.tags = self._request_body['tags']
            photo.remark = self._request_body['remark']
            Tags.add_tag(self._request_body['tags'])
            self.db_session.add(photo)
            self.db_session.commit()
        except Exception as e:
            self.logger.exception("%s %s Error: " % (self.__class__.__name__, self.request.method))
            self.return_json(500, data=u'服务器错误： %s' % str(e))
            self.db_session.rollback()
            return

        self.end_transaction()
        self.return_json(data=photo.json())