#coding:utf-8

import requests
import json
import para


url = 'https://payment.dev.bkjk-inc.com/deepfury/api/envelopes'
headers ={"Content-Type":"application/json"}
# data = {"no":para.no+str(1),"ownerId":"OLDAMAN"}
data = {"no":para.serial_no,"ownerId":"OLDAMAN"}


s = requests.get(url, headers=headers,params=data)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

rno = t[0]['id']

with open("parameter.json","r",encoding='utf-8') as f:
  d = json.load(f)


d['rno']=rno
with open("parameter.json","w",encoding='utf-8') as f:
  json.dump(d,f,ensure_ascii=False,indent=4)