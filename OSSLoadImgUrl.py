
# -*- coding: utf-8 -*-
# @file : OSSLoadUrl.py
# @Time : 2021-09-01 10:00
import uuid
import oss2
import datetime
import oss2.http


class OSSClient:
    def __init__(self, access_id: str = "", access_key: str = "", aliyun_endpoint: str = '',
                 private_bucket_name: str = ""):
        self.access_id = access_id
        self.access_key = access_key
        self.aliyun_endpoint = aliyun_endpoint
        self.private_bucket_name = private_bucket_name
        self.auth = oss2.Auth(self.access_id, self.access_key)
        self.bucket = oss2.Bucket(self.auth, self.aliyun_endpoint, self.private_bucket_name)
        self.bucket.create_bucket(oss2.models.BUCKET_ACL_PUBLIC_READ)

    def push_data_to_css(self, file_path, data):
        """
        上传内容
        :return: url
        """
        try:
            response = self.bucket.put_object(file_path, data)
            url = response.resp.response.url
            return url
        except Exception as err:
            local_time = ''.join(str(datetime.datetime.now().date()).split('-'))
            return f'https://****.oss-cn-hangzhou.aliyuncs.com/default/{local_time}.png'

    def upload_file_to_url(self, standard_no, img_content):
        stand_no = standard_no.replace(" ", "").replace(".", "").replace("/", "").replace(":", "").replace("\\*","").replace(
            "-", "").replace("?", "")
        file_name = f'default/{uuid.uuid4()}{stand_no}.png'
        url = self.push_data_to_css(file_name, img_content)
        return url


if __name__ == '__main__':
    with open('file_path', 'rb') as fp:
        resp = fp.read()
    oss_client = OSSClient()
    standard_no = 'huhdn sj fs'
    url = oss_client.upload_file_to_url(standard_no, resp)
    print(url)
