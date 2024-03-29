# -*- coding: utf-8 -*-
# @File     : QiNiuImgUrl.py
# @Software : PyCharm

# 一、
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
    



#     二、

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
from qiniu import BucketManager
import sys,time
import os
import msvcrt
import subprocess
from datetime import datetime


# you will get md_url in this file
result_file = "ss.txt"  

if os.path.exists(result_file):
    os.remove(result_file)
os.chdir(sys.path[0])

access_key = '********'
secret_key =  '********'
bucket_name =  '********'
bucket_url =  '********'
md_url_result = "md_url.txt"  # 链接保存的位置

img_suffix = ["jpg", "jpeg", "png", "bmp", "gif"]

def upload_img(bucket_name,file_name,file_path):
    # generate token
    token = q.upload_token(bucket_name, file_name, 3600)
    info = put_file(token, file_name, file_path)
    # delete local imgFile
    # os.remove(file_path)
    return

def get_img_url(bucket_url,file_name):
    # date=datetime.now().strftime('%Y%m%d_%H%M%S')
    # file_names = file_name+'?'+date
    img_url = 'http://%s/%s' % (bucket_url,file_name)
    # generate md_url
    md_url = "![%s](%s)\n" % (file_name, img_url)
    return md_url


def save_to_txt(bucket_url,file_name):
    url_before_save = get_img_url(bucket_url,file_name)
    # save to clipBoard
    addToClipBoard(url_before_save)
    # save md_url to txt
    with open(md_url_result, "a") as f:
        f.write(url_before_save)
    return

# save to clipboard
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

# get filename of .md in current index
def getMarkName(paths):
    f_list=os.listdir(paths)
    for i in f_list:
        name=os.path.splitext(i)[0]
        end=os.path.splitext(i)[1]
        if end=='.md':
            return name+'_'
    return 'markdown'


if __name__ == '__main__':
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    imgs = sys.argv[1:]
    
    
    for img in imgs:
        # name for img with local time 
        up_filename = getMarkName(os.getcwd().replace('\\','/')) + os.path.split(img)[1]
        upload_img(bucket_name,up_filename,img)
        save_to_txt(bucket_url,up_filename)
    
    

