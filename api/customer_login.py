# coding:utf8
import uuid
import time
from tornado import gen
from log.log_handler import logger
from utils.MD5 import md5
from utils.middleware import Prohandler
from database_driver.local_text_driver import read_local, update_local


class Customer_login(Prohandler):

    @gen.coroutine
    def post(self):
        user_name = self.data.get("user_name")
        pwd = self.data.get("pwd")
        user_token = self.data.get("user_token")

        if user_token:
            # 查库
            db_ret = read_local(1, user_name)
            if db_ret[-2] == user_token:
                return self.finish({"code": 200, "msg": "用户登陆成功"})

        if user_name is None or pwd is None:
            return self.finish({"code": 400,"msg": "用户名或密码为空"})

        # 查库
        db_ret = read_local(1, user_name)

        if db_ret is None:
            return self.finish({"code": 400,"msg": "用户名或密码错误"})
        elif db_ret[1] == user_name and db_ret[2] == md5(pwd):
            # 更新token, 此处未设置token过期时间，文本对比过期时间过于繁琐
            token = md5(uuid.uuid4())
            update_local(1, user_name, -2, token)
            logger.info("用户登陆成功")
            return self.finish({"code": 200,"msg": "用户登陆成功"})
        else:
            return self.finish({"code": 400,"msg": "用户名或密码错误"})
