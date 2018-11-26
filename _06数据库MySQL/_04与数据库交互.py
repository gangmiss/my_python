#coding=utf-8
from pymysql import *

try:
    conn = connect(host='192.168.145.130',port=3306,db='scholl',user='root',passwd='gangmiss',charset='utf8')
    cursors=conn.cursor()
    cursors.execute('insert into student values(5,%s,3,0,67.9)',["王刚"])
    conn.commit()
    cursors.close()
    conn.close()
except Exception as e:
    print(e.message)










