
import requests
import time
import json
import random
import var
import tk
import re


token = '5bd4215cf221910001c2d316'
url = 'http://cashierbe.dev.bkjk.cn/cashierbe/identity/confirmBinding'
headers ={"Content-Type":"application/json","Accept":"application/json"}
data = { "token":token,"confirmationCode": "888888"}

s = requests.get(url, headers=headers,params=data)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
# content = t['content']
# print(content)
# token = re.findall("token=(.+?)&bkuussso" ,content)
# print(token)