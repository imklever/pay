#coding:utf-8

'''
代付绑卡
https://payment.test.bkjk.com/
URL：/dfapi/unbind
请求参数：{"bindCardNo":""} 支付系统绑卡流水号
返回参数
{
"code": "0000",
"msg": "SUCCESS",
"data": "0" 0 为失败 1为成功
}
'''
#coding:utf-8
import requests
import json
import random
import time

url = 'https://payment.test.bkjk.com/dfapi/unbind'
headers ={"Content-Type":"application/json"}
data = {"bindCardNo":"181120143120068581162"}  #支付系统绑卡流水号

s = requests.post(url, data=json.dumps(data), headers=headers)
t = s.json()
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

