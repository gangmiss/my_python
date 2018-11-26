#coding=utf-8
from pymysql import *

class PyMysqlHelper(object):
    def __init__(self,host,port,user,passwd,charset="utf8"):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.charset=charset

    def open(self):
        try:
            self.conn=connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd)
            self.cursor=self.conn.cursor()
        except Exception:
            print("连接失败")

    def cud(self,sql,params):
        try:
            self.open()
            count=self.cursor.execute(sql,params)
            self.close()
            return count
        except Exception as e:
            print(e)

    def all(self,sql,params):
        try:
            self.open()
            result=self.cursor.mogrify(sql,params)
            self.close()
            return result
        except Exception as e:
            print(e)

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
