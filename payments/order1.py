#coding:utf-8

import requests
import time
import json
import random

# no = time.strftime("%Y%m%d%H%M%S", time.localtime())

url = 'http://cashierbe.dev.bkjk.cn/cashierbe/testOsg1'
headers ={"Content-Type":"application/json"}
data ={
  "merchantId": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229",
  "subMerchantId":"",
  "tradeNum": "20180821125955",
  "userInfo": {
    "partnerKey": "KE",
	"userId": "yht20180820",
	"userName": "杨海淘",
	"idNo": "51052219860514523X",
	"idType": "",
	"phone": "15811307862",
    "deviceInfo": {
      "ip": "223.223.184.146",
      "cityCode": "110000",
      "deviceType": "2311000000000",
      "eid": "",
      "appId": "",
      "port": "",
      "appType": "",
      "optType": "",
      "imei": "",
      "wlanMac": ""
    }
  },
  "payInfo": {
    "tradeName": "tradeName",
    "tradeDesc": "tradeDesc",
    "tradeRemarks":"",
    "tradeTime": "2018-05-23 00:00:00",
    "amount": 0.01,
	"paymentMethod":"2",
    "limitCreditCard":"true",
    "limitCreditPay":"false",
	"shareOrderInfos":
	{
	"merchantNo": "111",
	"amount":100,
	"feeAmount":10
	},
	"marketingInfo":
	{
	"fromMerchantNo": "T20180711000001",
    "toMerchantNo": "1001040",
	"amount": 0.99,
	"totalAmount":1
	}
  },
  "bizInfo": {
    "leaseInfo": {
      "orderId": "1111299",
      "monthRent": "100",
      "payRentMethod": "3",
      "deposit": "400",
      "loanAmount": "500",
      "months": "12",
      "cityCode": "110000",
      "address": "昆泰"
    },
    "flatInfo": {
      "subMerchantId":"111111",
      "brandId": "",
      "storeId": "20111",
      "roomId": "",
      "merchantName": "商户名称01",
      "brandName": "品牌01",
      "storeName": "",
      "cityCode": "110000",
      "address": "昆泰0110",
      "butlerName": "黄依胜",
      "butlerMobile": "17600483070",
      "receiveAcount": {
        "type": "PRIVATE",
        "name": "云浪",
        "bank": "中国银行",
        "cardNumber": "6217690700022480"
      }
    }
  },
  "callBackUrlArray": [{
      "name": "callbackUrl",
      "url": "callbackUrl",
      "type": "1"
    },
{
      "name": "payCompleteCallback",
      "url": "http://rf.feature.lianjia.com/pay/callback/bk",
      "type": "1"
    },
{
      "name": "pageReturnURL",
      "url": "http://rf.feature.lianjia.com/pay/callback/bk-quota/page-callback",
      "type": "1"
    },
    {
      "name": "pageReturnUrl",
      "url": "<h1/onmouseover=alert()>http://127.0.0.1:8080/cashierbe/test",
      "type": "2"
    }
  ]
}

s = requests.post(url, data=json.dumps(data), headers=headers)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
print(t['data'])

