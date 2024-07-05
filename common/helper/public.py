import random
import string


class Public(object):

    @staticmethod
    def random_str(num=6):
        """随机生成6位的数字+字母组合"""
        return ''.join([random.choice(string.digits + string.ascii_letters) for i in range(num)])
