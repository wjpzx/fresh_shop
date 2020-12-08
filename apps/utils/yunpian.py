import json
import requests
import random


# 生成随机验证码

class YunPian(object):
    def __init__(self,api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self,code,mobile):
        # 需要传递的参数
        params = {
            "apikey":self.api_key,
            "mobile":mobile,
            "text":"【王建鹏】您的验证码是%s。如非本人操作，请忽略本短信" % code
        }

        response = requests.post(self.single_send_url,data=params)
        re_dict = json.loads(response.text)
        return re_dict
