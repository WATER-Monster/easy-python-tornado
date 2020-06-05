# import pymysql
#
# from config.constans import db_host, db_port, db_user, db_password, database
#
#
# class MysqlOper:
#     def __init__(self):
#         self.client = pymysql.connect(host=db_host, port=db_port, user=db_user, password=db_password,
#                                       database=database,charset="utf8")
#         self.cursor = self.client.cursor()
#
#     def __enter__(self):
#         return self.cursor
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.client.commit()
#         self.cursor.close()
#         self.client.close()
