# coding:utf8
from tornado import gen
from utils.middleware import Prohandler
from database_driver.local_text_driver import read_local, update_local
from log.log_handler import logger


class Interview_status(Prohandler):

    @gen.coroutine
    def post(self):
        user_name = self.data.get("user_name")

        if user_name is None:
            return self.finish({"code": 400, "msg": "未检测到用户名称"})

        # 查询
        db_ret = read_local(1, user_name)
        status = db_ret[-3]

        logger.info("用户查询成功")

        return self.finish({"code": 200, "msg": "用户查询成功", "data":[{"status": status}]})