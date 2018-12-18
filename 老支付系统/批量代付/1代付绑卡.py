#coding:utf-8

'''
代付绑卡
https://payment.test.bkjk.com/dfapi/bind
URL：/dfapi/bind
请求参数：
{"accountName":"", 账户名称
"accountType":"",账户类型 01:对公账户 02: 对私银行卡 03: 对私存折 04: 对私信用卡
"appId":"",
"bankCardNo":"",银行卡号
"bankCnaps":"", 银行联行号
"bankName":"", 银行名称
"businessId":"",主体id
"operater":"" 操作人
}
返回：{
"code": "",0000 代表成功
"msg": "SUCCESS",
"data": {
"appId": "10005",
"bindCardNo": "", 支付系统绑卡流水号
"businessId": "2", 主体id
"bankCardNo": "", 卡号
"bankName": "", 银行名称
"accountName": "",
"bankCnaps": "",
"accountType": "",
"cardStatus": "OPEN", 绑卡状态 OPEN已绑卡 CLOSE已解绑
"createTime": "2018-08-01 17:23:26",
"updateTime": "2018-08-01 17:23:26",
"operater": "lr"
}
}
'''
#coding:utf-8
import requests
import json
import random
import time

url = 'https://payment.test.bkjk.com/dfapi/bind'
headers ={"Content-Type":"application/json"}
data = {
    "accountName":"test111200461",      #账户名称
    "accountType":"01",      #账户类型 01:对公账户 02: 对私银行卡 03: 对私存折 04: 对私信用卡
    "appId":"10007",
    "bankCardNo":"6222020200020507611",       #银行卡号
    "bankCnaps":"102100004960",        #银行联行号
    "bankName":"中国工商银行",         #银行名称
    "businessId":"18",      #主体id
    "operater":"test"         #操作人
    }
s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

