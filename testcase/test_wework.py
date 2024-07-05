from modules.requests_wework.wework_requests import WeworkModules


class TestWeworkRequests(object):

    # def test_wework_get_token_case(self):
    #     response = WeworkModules.get_wework_token_case()
    #     assert response.json().get("errcode") == 0, "未获取到企业微信 access token"
    #     assert response.json().get("errmsg") == "ok"

    def test_contact_list_create_member(self, get_wework_token):
        response = WeworkModules.contact_list_create_member(get_wework_token)
        assert response.json().get("errcode") == 0, "未成功创建通讯录用户"
        assert response.json().get("errmsg") == "created"
