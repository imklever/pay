'''
ADVANCE-提前；
NORMAL-正常；
OVERDUE-逾期；


# 装修还款信息
select n.`code` as financeNo, n.fund_loan_no as loanNo  from decoloan.orders n where n.code = 15367453284685;
select m.business_id as financeNo,m.account_periods,m.principal,m.interest,m.total,m.`status`from decoloan.repayment_order m where m.business_id = 15367453284685;

'''

import requests
import time
import json
import random
import var

print(var.timestamp)
url = 'http://cashierbe.dev.bkjk.cn/cashierbe/testOsg1'
Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLXRlc3QuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY4MjM1MDg5MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJmYmQwNmQ1NS0yN2ViLTQ5MGQtODkxYS03NThhYjBhYzRmZmQiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItdGVzdCJ9.KqLR2IWzIwVdA2ZbxQFQlfbv2yDZI6o_UawgTUBE-KA'

# XBKUUSSSOToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWZyZXNoX3Rva2VuX2V4cGlyZXNfaW4iOjMxMTA0MDAwLCJhdWQiOlsib2F1dGgyLXJlc291cmNlIl0sImFkZGl0aW9uYWxfaW5mbyI6InI1QXVBSXplMWdPaERWN0d6dG1qN3Q2Zk1LdzVpNEVWQWwwd0hXNkFkd3RNUm5GWldrNjJQL0svdjlUS1Z5MEhTNWRGMHk3UGIyZUtuQVE2ejdrL3hZdldJOEhtK2psRG5BdnNmWmZ3SytwaWxEMU94V0lLS1FTKzlRYVVvZE8yc3luY1dwKzBqbjFyZVBjN3pwZVY3TzlrWThhU3lkZ28zVDhBNE9lUE9HemdNYitMSW9GRFhkZFpQVHBTYVJyRGwwdU5Eck1heHFJPSIsInVzZXJfbmFtZSI6IjIxNCIsInBhcnRuZXJfa2V5IjoiQktKSyIsInNjb3BlIjpbInNuc2FwaV91c2VyaW5mbyIsInNuc2FwaV9wcml2YXRlaW5mbyJdLCJleHAiOjE1MzQ4Mzk5NzgsImF1dGhvcml0aWVzIjpbIlJPTEVfVVNFUiJdLCJqdGkiOiI3MGNlMmFmMS02OGVkLTQxNjEtOTlmZS0wMmU5NTQwMmNjMjgiLCJjbGllbnRfaWQiOiJia2prLTA4MjMifQ.cPLbecsFj5Yig0VuMwdkhCX9IzMQFsVbKJ9CdJXYluFqWX2bgoDz4Wb5ZkeZwPGfUs15hdtZ8sSXvVW6mE0SIYoSeE8w07hR-3emQSjf-r5vqZZFsFtXeVajKB_0sM5PpyMW_5NeC1mB1kulQxDecbeLH79IWrGFmfhnzq5OBGR-J1xyiofVSy16ZICXSeGoXZ5IFPxz8f5VbNgqDzBrAnrpQA_Runco97A7ERGIMAFXYTD3oheD6jWdQ5wClohmf4lZMr5Nj3_y4fOId2kNbOdr4MpAdUHACKze4_ydhqpimjLB7TBHt2BJxj1KJ5d73B2-DecwCEM3EUvEEzPk-w'
headers ={"Authorization":Authorization,"Content-Type":"application/json","sys-source":"CASHIER"}
data ={
  "merchantId": "e990ebd3-b56f-4b44-abfc-e4f54d6cf657",
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
    "amount": 1712.83,
    "paymentMethod":"0",
    "limitCreditCard":"false",
    "limitCreditPay":"true",
	"shareOrderInfos":[],
	"marketingInfo":
	{
	"fromMerchantNo": "T20180711000001",
    "toMerchantNo": "1001041",
	"amount": 1000,
	"totalAmount":7000
	}
  },
  "repayInfo": {
    "payeeCode": "39",
    "financeNo": "15332640653990",
    "loanNo": "FP15332640994224",
    "period": "3",
    "type": "OVERDUE",
    "periodNo": "code:15332640653990#periods:3",
    "amountDetails": [
      {
        "amount": 833.33,
        "type": "INTEREST"
      },
      {
        "amount": 879.50,
        "type": "FINE"
      },
      {
        "amount": 0.00,
        "type": "PRINCIPAL"
       }
    ]
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
      "merchantCode": "111",
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
      "url": "http://www.baidu.com",
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
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
print(t['data'])

