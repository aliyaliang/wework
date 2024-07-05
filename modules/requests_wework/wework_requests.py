import json
import random
import requests
import yaml

from common.helper import read_yaml
from common.helper.public import Public
# from conf.env_params import base_url
from requesturl.wework_request_url import RequestUrl


class WeworkModules(object):

    @staticmethod
    def get_wework_token_case():
        """
        发送请求获取企业微信 access_token
        corp_secret 为 获取通讯录的 secret
        """
        corp_info = read_yaml(file_path="testdata\\wework_data\\data_before_login.yml")
        corp_id = corp_info["corp_id"]
        corp_secret = corp_info["corp_secret"]
        payload = {"corpid": corp_id, "corpsecret": corp_secret}
        response = requests.get(url=RequestUrl.get_wework_token_uri(), params=payload)
        return response

    @staticmethod
    def contact_list_create_member(get_wework_token):
        """
        通讯录管理-成员管理-创建成员
        如果报错 IP 不在可信 IP 范围，加上可信 IP：
        https://work.weixin.qq.com/wework_admin/frame#apps/contactsApi
        """
        access_token = get_wework_token.json().get("access_token")
        param = {"access_token": access_token}
        member_info = read_yaml(file_path="testdata\\wework_data\\contact_list.yml")
        # data 数据放在 yaml 文件中，使用如下方法可以通过 key 获取 value，继续.get('skills', []).get(0, 'Not Found')读取第一个 skill
        mem_info_user_id = Public.random_str()
        mem_info_mobile = random.randint(13500000000, 13599999999)
        mem_info = member_info.get('contact_list_create_member', {})
        # 修改 yaml 文件中 userid 的值（key 存在修改 value，key 不存在则添加）
        if "userid" in mem_info and "mobile" in mem_info:
            mem_info["userid"] = mem_info_user_id
            mem_info["mobile"] = mem_info_mobile
        else:
            mem_info["userid"] = mem_info_user_id
            mem_info["mobile"] = mem_info_mobile
        # 将修改后的数据写回 yaml 文件
        with open("contact_list.yml", 'w') as file:
            yaml.dump(mem_info, file, default_flow_style=False)
        response = requests.post(url=RequestUrl.contact_list_create_member(), params=param, json=mem_info)
        # print('SAAA', response.json())
        return response


# WeworkModules.contact_list_create_member()
