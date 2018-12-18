#coding:utf-8

import requests
import time
import json
import random
import var

print(var.timestamp)
url = 'http://cashierbe.dev.bkjk.cn/cashierbe/testOsg1'
#测试e99
Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLXRlc3QuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY4MjM1MDg5MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJmYmQwNmQ1NS0yN2ViLTQ5MGQtODkxYS03NThhYjBhYzRmZmQiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItdGVzdCJ9.KqLR2IWzIwVdA2ZbxQFQlfbv2yDZI6o_UawgTUBE-KA'
#租赁8f
# Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLmNvbSIsInNjb3BlIjpbImN1c3RvZGlhbi5yZWFkIiwiY3VzdG9kaWFuLndyaXRlIiwiYWR2aXNlLnJlYWQiLCJhZHZpc2Uud3JpdGUiLCJjaGFubmVsLnJlYWQiLCJjaGFubmVsLndyaXRlIiwibWVyY2hhbnQucmVhZCIsIm1lcmNoYW50LndyaXRlIiwicGF5bWVudC5yZWFkIiwicGF5bWVudC53cml0ZSIsImNsZWFyaW5nLnJlYWQiLCJjbGVhcmluZy53cml0ZSIsInJlY29uY2lsaWF0aW9uLnJlYWQiLCJyZWNvbmNpbGlhdGlvbi53cml0ZSIsIm9yZGVyLnJlYWQiLCJvcmRlci53cml0ZSJdLCJleHAiOjM2NzMyNTI5MTMsImF1dGhvcml0aWVzIjpbIlJPTEVfTUVSQ0hBTlRfQURNSU4iXSwianRpIjoiYWY1MzQ0MWYtMTVhYS00NmU4LWIwMzktN2Y0MGNlZTllNWEzIiwiY2xpZW50X2lkIjoic2ltdWxhdG9yIn0.yZmCQz_jumD0JzIC0TQ1Snnw2AzrRJnM-Sln65Cy6hg'

headers ={"Authorization":Authorization,"Content-Type":"application/json","sys-source":"CASHIER"}
data ={
  "merchantId": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229", #租赁测试账户
  # "merchantId": "e990ebd3-b56f-4b44-abfc-e4f54d6cf657", #测试账户
  "subMerchantId":"",
  "tradeNum": var.timestamp,
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
    "amount": 10.00,
	"paymentMethod":"0",
    "limitCreditCard":"false",
    "limitCreditPay":"false",
    'limitWechatPay':"true",
	"shareOrderInfos":[],
	"marketingInfo":
	{
	"fromMerchantNo": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229",
    "toMerchantNo": "de8ea724-2ad5-40a8-83cf-beeb32f60891",
	"amount": 200.00,
	"totalAmount":210.00
	},
    "creditChannel":"JD_QUOTA",
    "jdCreditUrl":"https://www.jd.com",
    "jdCreditAmount":10000
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
      "merchantCode":"111",
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
      "butlerMobile": "17600483071",
      "receiveAcount": {
        "type": "PRIVATE",
        "name": "云浪",
        "bank": "中国银行",
        "cardNumber": "6217690700022480"
      }
    }
  },
  "callBackUrlArray": [
    {
      "name": "callbackUrl",
      "url": "http://www.hao123.com",
      "type": "1"
    },
    {
      "name": "payCompleteCallback",
      "url": "https://www.sina.com.cn",
      "type": "1"
    },
    {
      "name": "pageReturnURL",
      "url": "https://www.163.com",
      "type": "1"
    },
      {
          "name": "cancelPageUrl",
          "url": "https://www.58.com",
          "type": "1"
      },
    {
      "name": "pageReturnUrl",
      "url": "https://www.baidu.com",
      "type": "2"
    }
  ]
}

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
print(t['data'])

