#coding:utf-8

'''
代付绑卡
https://payment.test.bkjk.com/
URL：/dfapi/pagecard
请求参数:{"businessId":"1","pageSize": "10", "pageNum": "1",
"bindCardNo": "180724171310644178102",
"cardStatus": "CLOSE",
"bankCardNo": "6214920208566047",
"accountType": "02",
"endTime":"1533200776000",
"startTime":"1532423788000",
"merchantName":"德祐a"
}
'''
#coding:utf-8
import requests
import json
import random
import time

url = 'https://payment.test.bkjk.com/dfapi/pagecard'
headers ={"Content-Type":"application/json"}
data = {
    "businessId":"1", #有问题
    "pageSize": "10",  #***
    "pageNum": "1",    #***
    "bindCardNo": "181108151153457254313", #有问题
    "cardStatus": "OPEN", #有问题
    "bankCardNo": "6222020200020",
    "accountType": "01", #有问题
    "endTime":"",
    "startTime":"",
    "merchantName":"北京中融信融资担保有限公司"
}
s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

# print(time.localtime())