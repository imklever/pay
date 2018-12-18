#coding:utf-8

import requests
import time
import json
import random

# no = time.strftime("%Y%m%d%H%M%S", time.localtime())

Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLWNyZWQuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY3NTY1Mjc1MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJkYTZlZTU3ZC1kNTdkLTQyNTQtOWQ3MC1lZmFjY2Y5YmZjODYiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItY3JlZCJ9.TiB739KogijD3AIg0rNTJFtfXeEpheZIUp5jLI_NFYQ'
url = 'http://archimonde.dev.bkjk.cn/archimonde/api/merchants'
headers ={"Authorization":Authorization,"Content-Type":"application/json","Accept":'application/json'}
data = {
  # "merchantId":"1001164",
  "no":"20180810153730",
  # "parentMerchantId":"20180724143033647986",
  "paymentMerchantNo":"1",  ###
  "paymentType":"LFTPAY",           ####
  "paymentPrivateKey": "111", ####
  "paymentApiKey": "1",        ####
  "paymentSalt": "111",        ###
  "legalPersonName": "string",
  "legalPersonPhone": "15808100009",
  "legalPersonIdNo": "993703196207205609",
  "legalPersonIdType": "PASSPORT",
  "legalPersonIdBeginDate": "2018-01-01",
  "legalPersonIdEndDate": "9999-01-01",
  "legalPersonPictureUrls": "http://img.zcool.cn/community/0117e2571b8b246ac72538120dd8a4.jpg@1280w_1l_2o_100sh.jpg;http://t2.hddhhn.com/uploads/tu/201612/98/st93.png",
  "type": "PERSONAL",
  "name": "贝壳小贷测试20180810153730",
  "address": "上海市新天地贝壳小贷",
  "email":"20180810153730@2018.com",
  "uniform":"false",
  "organizationNo": "test",
  "taxNo": "test",
  "licenseNo": "test20180810153730",
  "licenseBeginDate": "2018-01-01",
  "licenseEndDate": "9999-01-01",
  "licenseScope": "string",
  "licensePictureUrls": "test",
  "taxPictureUrls": "test",
  "organizationPictureUrls": "test",
  "bankAccountPictureUrls": "test",
  "contactPersonName": "string",
  "contactPersonPhone": "17808100009",
  "contactPersonEmail": "20180810153730@2.com",
  "bankAccountType": "PRIVATE",   ######
  "bankAccountName": "11",  #####
  "bankAccountNo": "111",   #####
  "bankName": "1111",   ######
  "bankBranchName": "111",  ######
  "remarks": "12",
  "callbackUrl":"string"
}

s = requests.post(url, data=json.dumps(data), headers=headers)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


