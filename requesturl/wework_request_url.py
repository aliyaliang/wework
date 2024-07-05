# -*- coding: utf-8 -*-
from conf.env_params import Env


class RequestUrl(object):

    base_url = Env.testing_environment()

    @staticmethod
    def get_wework_token_uri():
        base_url_instance = Env()
        base_url, corp_id, corp_secret = base_url_instance.testing_environment()
        return base_url + "/cgi-bin/gettoken"

    @staticmethod
    def contact_list_create_member():
        base_url_instance = Env()
        base_url, corp_id, corp_secret = base_url_instance.testing_environment()
        return base_url + "/cgi-bin/user/create"
