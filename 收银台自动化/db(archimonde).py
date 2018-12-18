#coding:utf-8

import pymysql.cursors

serial_no = '20181129134931'

# 连接数据库
connect = pymysql.Connect(
    host='172.29.10.50',
    port=3307,
    user='archimonde',
    passwd='0TtYBNAOD2So',
    db='archimonde',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

sql = "select * from payment_transaction where serial_no = '%s'"
data = serial_no
cursor.execute(sql % data)
# for row in cursor.fetchall():
#     print("%s" % row)
t = cursor.fetchall()
print(t)
# s1 = t[0][0]
# s2 = t[0][1]
# print("系统号:"+str(s1))
# print("姓名:"+str(s2))
# print("密码:BKJK@test")


cursor.close()
connect.close()
