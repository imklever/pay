'''
签约代扣测试账号
卡号:6288888888888888
户名:张小小
身份证:410482198302100584
手机号:13201569405
验证码:888888
userId = 56251/bab203bd862b4d8594b553a4742a5dab
'''

import requests
import time
import json
import random
import var
import tk
import re

print(var.timestamp)
url = 'http://api.dev.bkjk.cn/cashierbe/identity/create'
headers ={"X-BK-UUSSSO-Token":tk.token,"Content-Type":"application/json","Accept":"application/json"}
data = {
 "merchantId": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229", #租赁测试账户
 # "merchantId": "e990ebd3-b56f-4b44-abfc-e4f54d6cf657",  # 测试账户
 # "no": "6228480028516174977",
 "no": var.timestamp,
 # "name": "测试",
 "name": "张小小",
 "idNo": "410482198302100584",
 # "idNo": "340826198812291811",
 # "userId": "dsad",
  "userId": "bab203bd862b4d8594b553a4742a5dab",
 "redirectUrl": "https://www.hao123.com",
 "callBackUrl": "https://www.baidu.com",
 "paymentType": "LFTPAY"
}

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)dccx
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
content = t['content']
print(content)
token = re.findall("token=(.+?)&bkuussso" ,content)
print(token)
