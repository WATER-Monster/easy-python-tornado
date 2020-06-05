# coding:utf8

"""
url映射
"""
from api.customer_login import Customer_login
from api.customer_config import Customer_config
from api.interview_management import Interview_management
from api.interview_status import Interview_status

url_map = [
    (r"/login", Customer_login),
    (r"/config", Customer_config),
    (r"/management", Interview_management),
    (r"/status", Interview_status),
]
