# -*- coding: utf-8 -*-
from conf.env_params import Env


class RequestUrl(object):

    @classmethod
    def get_env_info(cls):
        base_url_instance = Env()
        return base_url_instance.testing_environment()

    @staticmethod
    def get_uri(endpoint):
        base_url, corp_id, corp_secret = RequestUrl.get_env_info()
        return base_url + endpoint

    @staticmethod
    def get_wework_token_uri():
        return RequestUrl.get_uri("/cgi-bin/gettoken")

    @staticmethod
    def contact_list_create_member():
        return RequestUrl.get_uri("/cgi-bin/user/create")
