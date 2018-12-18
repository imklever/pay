'''
-- 分账商户号
SELECT id, settle_id, status, created_time FROM merchant where settle_id <> ' ';
'''

import requests
import time
import json
import random
import var

print(var.timestamp)
url = 'http://cashierbe.dev.bkjk.cn/cashierbe/testOsg1'
# XBKUUSSSOToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWZyZXNoX3Rva2VuX2V4cGlyZXNfaW4iOjMxMTA0MDAwLCJhdWQiOlsib2F1dGgyLXJlc291cmNlIl0sImFkZGl0aW9uYWxfaW5mbyI6InI1QXVBSXplMWdPaERWN0d6dG1qN3Q2Zk1LdzVpNEVWQWwwd0hXNkFkd3RNUm5GWldrNjJQL0svdjlUS1Z5MEhTNWRGMHk3UGIyZUtuQVE2ejdrL3hZdldJOEhtK2psRG5BdnNmWmZ3SytwaWxEMU94V0lLS1FTKzlRYVVvZE8yc3luY1dwKzBqbjFyZVBjN3pwZVY3TzlrWThhU3lkZ28zVDhBNE9lUE9HemdNYitMSW9GRFhkZFpQVHBTYVJyRGwwdU5Eck1heHFJPSIsInVzZXJfbmFtZSI6IjIxNCIsInBhcnRuZXJfa2V5IjoiQktKSyIsInNjb3BlIjpbInNuc2FwaV91c2VyaW5mbyIsInNuc2FwaV9wcml2YXRlaW5mbyJdLCJleHAiOjE1MzQ4Mzk5NzgsImF1dGhvcml0aWVzIjpbIlJPTEVfVVNFUiJdLCJqdGkiOiI3MGNlMmFmMS02OGVkLTQxNjEtOTlmZS0wMmU5NTQwMmNjMjgiLCJjbGllbnRfaWQiOiJia2prLTA4MjMifQ.cPLbecsFj5Yig0VuMwdkhCX9IzMQFsVbKJ9CdJXYluFqWX2bgoDz4Wb5ZkeZwPGfUs15hdtZ8sSXvVW6mE0SIYoSeE8w07hR-3emQSjf-r5vqZZFsFtXeVajKB_0sM5PpyMW_5NeC1mB1kulQxDecbeLH79IWrGFmfhnzq5OBGR-J1xyiofVSy16ZICXSeGoXZ5IFPxz8f5VbNgqDzBrAnrpQA_Runco97A7ERGIMAFXYTD3oheD6jWdQ5wClohmf4lZMr5Nj3_y4fOId2kNbOdr4MpAdUHACKze4_ydhqpimjLB7TBHt2BJxj1KJ5d73B2-DecwCEM3EUvEEzPk-w'
headers ={"Content-Type":"application/json","X-BK-UUSSSO-Token":var.XBKUUSSSOToken,"sys-source":"CASHIER"}
data ={
  # "merchantId": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229", #租赁测试账户
  "merchantId": "e990ebd3-b56f-4b44-abfc-e4f54d6cf657",  # 测试账户
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
    "amount": 500.00,
	"paymentMethod":"0",
    "limitCreditCard":"false",
    "limitCreditPay":"true",
    "shareOrderInfos": [
      {
      "merchantNo": "20180823185450619609",
      "amount":20.00,
      "feeAmount": 20.00
      },
      {
        "merchantNo": "1001224",
        "amount": 30.00,
        "feeAmount": 30.00
      },
      {
        "merchantNo": "1001194",
        "amount": 50.00,
        "feeAmount": 50.00
      }
    ],
	"marketingInfo":
      {
        "fromMerchantNo": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229",
        "toMerchantNo": "de8ea724-2ad5-40a8-83cf-beeb32f60891",
        "amount": 10.00,
        "totalAmount": 100.00
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

