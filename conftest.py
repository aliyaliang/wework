import pytest
import requests
from conf.env_params import Env
from requesturl.wework_request_url import RequestUrl


@pytest.fixture
def get_wework_token():
    """
    发送请求获取企业微信 access_token
    corp_secret 为 获取通讯录的 secret
    """
    testing_env_instance = Env()
    base_url, corp_id, corp_secret = testing_env_instance.testing_environment()
    payload = {"corpid": corp_id, "corpsecret": corp_secret}
    response = requests.get(url=RequestUrl.get_wework_token_uri(), params=payload)
    return response

