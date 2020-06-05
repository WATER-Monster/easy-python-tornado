# coding:utf8
from tornado import gen
from utils.middleware import Prohandler
from database_driver.local_text_driver import read_local, update_local
from log.log_handler import logger


class Customer_config(Prohandler):

    @gen.coroutine
    def post(self):
        user_name = self.data.get("user_name")
        user_interview = self.data.get("user_interview")

        if user_name is None:
            return self.finish({"code": 400, "msg": "未检测到用户名称"})

        if user_interview is None:
            return self.finish({"code": 400, "msg": "未检测到修改内容"})

        # 改库
        update_local(1, user_name, -3, user_interview)

        logger.info("用户修改成功")

        return self.finish({"code": 200, "msg": "用户修改成功"})