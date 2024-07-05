# -*- coding: utf-8 -*-


class RequestUrl(object):

    @staticmethod
    def get_wework_token_uri():
        return "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

    @staticmethod
    def contact_list_create_member():
        return "https://qyapi.weixin.qq.com/cgi-bin/user/create"
