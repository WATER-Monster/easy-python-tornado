# coding:utf8
import os

import tornado.web
import tornado.httpserver
from tornado.options import define, options
from config import url_map, constans

define("port", default=constans.port, type=int)
dir_str = os.path.dirname(__file__)
if dir_str.find("config"):
    dir_str = dir_str + "/../"
settings = {
    "static_path": os.path.join(dir_str, "static")
}

app = tornado.web.Application(
    handlers=url_map.url_map,
    **settings
)

http_server = tornado.httpserver.HTTPServer(app)
http_server.bind(options.port)

# linux 系统下建议使用 4-8 进程启动，windows系统下不支持epoll,只能单进程启动
http_server.start(1)
