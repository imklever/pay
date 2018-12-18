#coding:utf-8

import requests
import json
import var
import data

print(var.timestamp)
url = 'http://cashierbe.dev.bkjk.cn/cashierbe/testOsg1'
headers ={"Content-Type":"application/json"}
data ={
  "merchantId": data.merchantId, #租赁测试账户
  # "merchantId": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229",  # 租赁测试账户
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
    "amount": data.amount,
	"paymentMethod":data.paymentMethod,
    "limitCreditCard":"false",
    "limitCreditPay":"false",
    "appId": "wx843fd86f21127636",
    # wx7d06af9eda102f32,wx843fd86f21127636
    "openId": "oxBhw1k3ntgG28CtlMn3N0P1WI7o",
	"shareOrderInfos":[],
	"marketingInfo":
	{
	"fromMerchantNo": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229",
    "toMerchantNo": "de8ea724-2ad5-40a8-83cf-beeb32f60891",
	"amount": data.amount1,
	"totalAmount":data.totalAmount
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
token = t['data'].split("/")[-1]
# print(token)



d = {'no':var.timestamp,'token':token}
with open("parameter.json","w",encoding='utf-8') as f:
  json.dump(d,f,ensure_ascii=False,indent=4)