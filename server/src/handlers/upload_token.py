#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Luffy Liu
Date   : 15-4-5
Email  : luffy.liu@maichuang.net
'''

import time
from qiniu import Auth
from hashlib import md5
from src.settings import AK, SK, BUCKET_NAME, UPLOAD_PYOLIC
from src.handlers.basic import BasicHandler
from src.models.photo import Photos

BASE_HTML = """
    <form method="post" action="http://upload.qiniu.com/"
    enctype="multipart/form-data">
    <input name="token" type="hidden" value="%s">
    <input name="file" type="file" />
    <input type="submit" value="Submit" />
    <input name="key" type="hidden" value="%s">

    </form>
"""

def gen_token_and_filename():
    q = Auth(AK, SK)

    #防止照片文件名重复,采用对时间md5后的值当作七牛中的key
    filename = md5(str(time.time())).hexdigest()
    # 上传策略仅指定空间名和上传后的文件名，其他参数仅为默认值
    token = q.upload_token(BUCKET_NAME, filename, policy=UPLOAD_PYOLIC)

    return token, filename

def gen_uplaod_html(token, filename):
    upload_html = BASE_HTML % (token, filename)
    f = open('/tmp/upload.html', 'w+')
    f.write(upload_html)
    f.close()


class UploadTokenHandler(BasicHandler):

    def check_get(self):
        return True

    def get(self):
        if not self.check_get():
            return

        token, filename = gen_token_and_filename()
        gen_uplaod_html(token, filename)

        # self.start_transaction()
        # try:
        #     photo = Photos()
        #     photo.hash_id = filename
        #     self.db_session.add(photo)
        #     self.db_session.commit()
        # except Exception as e:
        #     self.logger.exception("%s %s Error: " % (self.__class__.__name__, self.request.method))
        #     self.return_json(500, data=u'服务器错误： %s' % str(e))
        #     self.db_session.rollback()
        #     return
        #
        # self.end_transaction()
        self.return_json(data={"token": token, 'key': filename})