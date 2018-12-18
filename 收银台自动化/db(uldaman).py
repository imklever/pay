#coding:utf-8

import pymysql.cursors

no = '20181129134931'

# 连接数据库
connect = pymysql.Connect(
    host='172.29.10.50',
    port=3307,
    user='uldaman',
    passwd='QhsbSLIqH0jA',
    db='uldaman',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

sql = "select id,no,status,amount from business_orders where no = '%s'"
data = no
cursor.execute(sql % data)

t = cursor.fetchall()
# print(t)
id = t[0][0]
no = t[0][1]
status = t[0][2]
amount = t[0][3]
print("++++++++++business_orders表++++++++++")
print("id:"+id)
print("no:"+no)
print("status:"+status)
print("amount:"+str(amount))

sql1 = "select id,serial_no,status,order_id,amount from payment_orders where order_id = '%s'"
cursor.execute(sql1 % id)
# for row in cursor.fetchall():
#     print("%s" % row)
t1 = cursor.fetchall()
print("++++++++++payment_orders表++++++++++")
# print(t1)
for i in range(len(t1)):
    print('第'+str(i+1)+'条记录:')
    print('id:'+ t1[i][0])
    print('serial_no:' + t1[i][1])
    print('status:' + t1[i][2])
    print('order_id:' + t1[i][3])
    print('amount:' + str(t1[i][4]))

cursor.close()
connect.close()

