# coding:utf8
import json
from tornado.web import RequestHandler


class Prohandler(RequestHandler):

    def initialize(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers',
                        'X-Requested-With,Referer,Accept,Origin,User-Agent,Content-Type')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

    def options(self):
        self.set_status(200)
        self.finish()

    def prepare(self):
        if self.request.method == "POST":
            try:
                self.data = json.loads(self.request.body.decode())
            except Exception:
                return self.finish({"code": 301, "msg": "错误的json格式"})
