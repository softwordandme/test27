# -*- coding: utf-8 -*-
import cx_Oracle
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'     # 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
db = cx_Oracle.connect('developer/comber@192.168.32.203:1521/bhtest')

# 输出数据库版本号print db.version

c = db.cursor()   # 获取cursor()
sql = 'select * from rule where status = 1'

result = c.execute(sql)  # 默认不返回查询结果集， 返回数据记录数。
des = str(c.description).decode("string_escape")    # 获取表头
print des

start = "我们213"
result = start

x = c.execute(sql)  # 使用cursor()操作查询

for i in x.fetchall():       # 展示查询结果，fetchone函数是获得一行结果，fetchall函数是获得所有行结果。均为元组
    key = str(i[1]).decode("string_escape")
    value = str(i[2]).decode("string_escape")
    res = result.replace(key, value)
    result = res

print "开始为:" + start + "\r\n最终结果为:" + result
c.close()                              # 关闭cursor()
db.close()                           # 关闭数据库连接