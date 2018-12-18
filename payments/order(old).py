#coding:utf-8

import requests
import time
import json
import random

#####入参#####
#####请求参数######
merchantId = '8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229'
# subMerchantId = 'subMerchantId'
tradeNum = '20180704162707'


####用户设备信息deviceInfo###
ip = "223.223.184.146"
cityCode = "110000"
deviceType = "2311000000000"
eid = ""
appId = ""
port = ""
appType = ""
optType = ""
imei = ""
wlanMac = ""

###用户信息userInfo###
partnerKey = 'KE'
userId = 'yht2'
userName = '杨海淘'
idNo = '51052219860514523X'
idType = ''
phone = '15811307862'

###支付信息payInfo####
tradeName = "tradeName"
tradeDesc = "tradeDesc"
tradeTime = "2018-05-23 00:00:00"
amount = 20000
transactionType = ""
useCredit = "1"
creditInfo = ""
# paymentMethod = "paymentMethod"
# shareOrderInfos = "shareOrderInfos"
# shareOrderInfos.merchantNo = "shareOrderInfos.merchantNo"
# shareOrderInfos.amount = "shareOrderInfos.amount"
# shareOrderInfos.feeAmount = "shareOrderInfos.feeAmount"
# marketingInfo = "marketingInfo"
# marketingInfo.merchantNo = "marketingInfo.merchantNo"
# marketingInfo.amount = "marketingInfo.amount"
# marketingInfo.totalAmount = "marketingInfo.totalAmount"

#####租约信息leaseInfo#####
orderId = "1111299"
monthRent = "100"
payRentMethod = "3"
deposit = "400"
loanAmount = "500"
months = "12"
cityCode = "110000"
address = "昆泰"

###公寓信息flatInfo#####
merchantCode = "20100"
brandId = ""
storeId = "20111"
roomId = ""
merchantName = "商户名称01"
brandName = "品牌01"
storeName =  ""
cityCode = "110000"
address = "昆泰0110"
butlerName = "黄依胜"
butlerMobile = "17600483070"
# receiveAcount = ""
receiveAcounttype = "PRIVATE"
receiveAcountname = "云浪"
receiveAcountbank = "中国银行"
receiveAcountcardNumber = "6217690700022480"

#####回调信息callBackInfo#######
# # callBackUrlArray = "callBackUrlArray"
# name = 'callbackUrl'
# url = 'callbackUrl'
# type = 'type'
callbackUrlname = 'callbackUrl'
callbackUrlurl = 'callbackUrl'
callbackUrltype = '1'
payCompleteCallbackname = 'payCompleteCallback'
payCompleteCallbackurl = 'http://rf.feature.lianjia.com/pay/callback/bk'
payCompleteCallbacktype = '1'
pageReturnURLname = 'pageReturnURL'
pageReturnURLurl = 'http://rf.feature.lianjia.com/pay/callback/bk-quota/page-callback'
pageReturnURLtype = '1'
pageReturnUrlname = 'pageReturnUrl'
pageReturnUrlurl = '<h1/onmouseover=alert()>http://127.0.0.1:8080/cashierbe/test'
pageReturnUrltype = '2'



###用户信息userInfo###
userInfo = {
"partnerKey": partnerKey,
"userId": userId,
"userName": userName,
"idNo": idNo,
"idType": idType,
"phone": phone,
"deviceInfo": {
  "ip": ip,
  "cityCode": cityCode,
  "deviceType": deviceType,
  "eid": eid,
  "appId": appId,
  "port": port,
  "appType": appType,
  "optType": optType,
  "imei": imei,
  "wlanMac": wlanMac
  }
}




###支付信息payInfo####
payInfo = {
"tradeName": tradeName,
"tradeDesc": tradeDesc,
"tradeTime": tradeTime,
"amount": amount,
"transactionType": transactionType,
"useCredit": useCredit,
"creditInfo": creditInfo
}



####租约信息#####
leaseInfo = {
"orderId": orderId,
"monthRent": monthRent,
"payRentMethod": payRentMethod,
"deposit": deposit,
"loanAmount": loanAmount,
"months": months,
"cityCode": cityCode,
"address": address
}

####打款账户####
receiveAcount = {
"type": receiveAcounttype,
"name": receiveAcountname,
"bank": receiveAcountbank,
"cardNumber": receiveAcountcardNumber
}

#######公寓信息######
flatInfo = {
"merchantCode": merchantCode,
"brandId": brandId,
"storeId": storeId,
"roomId": roomId,
"merchantName": merchantName,
"brandName": brandName,
"storeName": storeName,
"cityCode": cityCode,
"address": address,
"butlerName": butlerName,
"butlerMobile": butlerMobile,
"receiveAcount": receiveAcount
}

###业务信息###
bizInfo = {"leaseInfo":leaseInfo,"flatInfo":flatInfo}

#####回调信息######
callbackUrl = {
"name": callbackUrlname,
"url": callbackUrlurl,
"type": callbackUrltype
}
payCompleteCallback = {
"name": payCompleteCallbackname,
"url": payCompleteCallbackurl,
"type": payCompleteCallbacktype
}
pageReturnURL = {
"name": pageReturnURLname,
"url": pageReturnURLurl,
"type": pageReturnURLtype
}
pageReturnUrl = {
"name": pageReturnUrlname,
"url": pageReturnUrlurl,
"type": pageReturnUrltype
}

callBackUrlArray = [callbackUrl,payCompleteCallback,pageReturnURL,pageReturnUrl]



###############post请求#########################

url = 'http://cashierbe.dev.bkjk.cn/cashierbe/testOsg1'
headers ={"Content-Type":"application/json"}

data ={
  "merchantId": merchantId,
  "tradeNum": tradeNum,
  "userInfo": userInfo,
  "payInfo": payInfo,
  "bizInfo": bizInfo,
  "callBackUrlArray": callBackUrlArray
}

s = requests.post(url, data=json.dumps(data), headers=headers)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


