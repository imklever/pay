#coding:utf-8
import json

with open("config/data.json","r",encoding='utf-8') as f1:
  d = json.load(f1)

merchantId = d["merchantId"]
amount = d["amount"]
amount1 = d["amount1"]
totalAmount = d["totalAmount"]
paymentMethod = d["paymentMethod"]

# for i in d:
#   i=d[i]
