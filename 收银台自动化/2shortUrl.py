#coding:utf-8

import requests
import json
import para


url1 = 'http://dev.cashier.zufangzi.com/cashierbe/shortUrl/'
token = para.token
url = url1+token
headers ={"Content-Type":"application/json"}
s = requests.get(url, headers=headers)
print(s.url)
print(s.status_code)
jwt = s.url.split("=")[2]
# print(jwt)
Authorization = 'Bearer '+jwt
# print(Authorization)

with open("parameter.json","r",encoding='utf-8') as f:
  d = json.load(f)
  # print(d)

d['Authorization']=Authorization
# print(d)
with open("parameter.json","w",encoding='utf-8') as f:
  json.dump(d,f,ensure_ascii=False,indent=4)