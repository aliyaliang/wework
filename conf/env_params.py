# base_url = "https://qyapi.weixin.qq.com"
from conf.set_env import env


class Env(object):
    @staticmethod
    def testing_environment():
        base_url = None
        if env == "development":
            # 设置开发环境
            print("Running in development environment")
            base_url = "https://qyapi.weixin.qq.com"
        elif env == "staging":
            # 设置预生产环境
            print("Running in staging environment")
            base_url = "staging 环境 url"
        elif env == "production":
            # 设置生产环境
            print("Running in production environment")
            base_url = "生产环境 url"
        # print(base_url)
        return base_url


# Env.testing_environment()
