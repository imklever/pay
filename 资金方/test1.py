#coding:utf-8

import requests
import json
import random
import time
import var

timestamp = var.timestamp
timestamp1 = var.timestamp1
url = 'http://fund.test.bkjk.cn/fund/api/exam/channelRouteExamine'
headers ={"Content-Type":"application/json"}
data = {
    "productLine": "L_DECORATION_FINANCE",
	"productId":"ZXFQ20171111001",
	"productName":"装修贷",
	"financeOrderNo": timestamp,
	"fundLoanNo":timestamp1,
	"loanApplyTime":"20180824094412123",
	"notifyUrl":"http://localhost:8280/fund/api/exam/xxxxx",
	"loanInfo":{
					"loanContractNo":timestamp,
					"loanAmount":1200,
					"loanTerm":12,
					"termUnit":"MONTH",
					"signRate":0.6,
			    	"repayCycle":"0",
			    	"repayMode":"4"
				},
	"borrowerInfo":{
					"borrowerName":"张四",
					"borrowerAge":30,
					"borrowerSex":"FEMALE",
					"telePhone":"17331791160",
					"idType":"ID_CARD",
					"idCardNo":"130984199009075161",
			    	"maritalStatus":"10",
			    	"livingCity":"110100",
			    	"livingAddress":"110100",
			    	"postCode":"100020",
			    	"careerType":"8"
				}
}

print("路由审核。。。。。。。。。。")

s = requests.post(url, data=json.dumps(data), headers=headers)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


time.sleep(2)

print("审核查询。。。。。。。。。。")

url = 'http://fund.test.bkjk.cn/fund/api/exam/channelRouteExamineQuery'
headers ={"Content-Type":"application/json"}
data = {
	"financeOrderNo":timestamp,
	"fundLoanNo":timestamp1
	}

s = requests.post(url, data=json.dumps(data), headers=headers)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)