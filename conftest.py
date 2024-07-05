import pytest
import requests
from common.helper import read_yaml
# from conf.env_params import base_url
from requesturl.wework_request_url import RequestUrl


@pytest.fixture
def get_wework_token():
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


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="development", help="set environment: development, staging, or production"
    )
