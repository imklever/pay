#coding:utf-8

import requests
import json
import random
import time
import test1

url = 'http://fund.test.bkjk.cn/fund/api/exam/channelRouteExamineQuery'
headers ={"Content-Type":"application/json"}
data = {
	"financeOrderNo": test1.timestamp,
	"fundLoanNo":test1.timestamp1
	}

s = requests.post(url, data=json.dumps(data), headers=headers)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

