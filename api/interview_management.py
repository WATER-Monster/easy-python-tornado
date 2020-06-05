# coding:utf8
from tornado import gen
from utils.middleware import Prohandler
from database_driver.local_text_driver import read_local, update_local
from log.log_handler import logger


class Interview_management(Prohandler):

    @gen.coroutine
    def post(self):
        user_name = self.data.get("user_name")
        aid_user_name = self.data.get("aid_user_name")
        user_auth = self.data.get("user_auth")

        # 查询用户权限
        db_ret = read_local(1, user_name)

        # 权限不足
        if user_auth is not None and db_ret[-4] != "admin":
            return self.finish({"code": 400, "msg": "用户权限不足，无法修改"})

        # 改库
        update_local(1, aid_user_name, -4, user_auth)

        logger.info("用户修改成功")

        return self.finish({"code": 200, "msg": "用户修改成功"})