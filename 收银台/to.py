#coding:utf-8

import requests
import time
import json
import random
import var

# print(var.XBKUUSSSOToken)
# print(var.timestamp)
url = 'http://dev-ewallet-api.ehomepay.com.cn/ewallet/cashier/standardPay'
headers ={"Content-Type":"application/json","X-BK-UUSSSO-Token":var.XBKUUSSSOToken}
data ={
	"tpId":"T201801250010001001",
	"merchantNo":"T201801221000002",
	"orderNo":var.timestamp,
	"tradeNo":var.timestamp,
	"tradeType":"01",
	"userInfo":{
		"partnerUid":"12345",
		"partnerKey":"KE"
	},
	"payInfo":{
		"tradeName":"tradeDesc",
		"tradeDesc":"tradeDesc",
		"tradeTime":"2018-08-21 14:41:06",
		"amount":0.01,
		"totalAmount":0.01
	},
	"callBackInfo":{
		"callbackUrl":"http://123.com",
		"pageReturnUrl":"http://123.com",
		"cancelPageUrl":"http://123.com"
	}
}

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
print("rembId: "+t['content']['rembId'])

rembId = t['content']['rembId']