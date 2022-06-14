# -*- coding: utf-8 -*-
# @File     : QiNiuImgUrl.py
# @Software : PyCharm
from qiniu import Auth, put_file

access_key = ''
secret_key = ''

# 生成上传凭证
def qiniu_token(bucked_name, key):
    q = Auth(access_key=access_key, secret_key=secret_key)
    token = q.upload_token(bucked_name, key)
    return token

def upload_img(file_path, file_name):
    """
    收集本地信息到云服务器上
    参考地址：https://developer.qiniu.com/kodo/sdk/1242/python
    """
    bucked_name = 'kapai'
    # 指定图片名称,上传后保存的文件名
    token = qiniu_token(bucked_name, file_name)
    ret, info = put_file(token, file_name, file_path)
    image_file = f'https://xxx.xxx.com/' + ret.get('key')
    return image_file
    
