# coding:utf8

from log.log_handler import logger
from config.config import http_server
import tornado.ioloop


if __name__ == "__main__":
    logger.info("服务器启动")
    tornado.ioloop.IOLoop.instance().start()
