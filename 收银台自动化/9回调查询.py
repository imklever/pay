#coding:utf-8
'''

'''

import requests
import json
import para

# id = '5bff7e2d354c2d00075ec471'
url1 = 'https://payment.dev.bkjk-inc.com/deepfury/api/envelopes/'
url2 = '/records'
url = url1 + para.rno + url2
print(url)
headers ={"Content-Type":"application/json"}

s = requests.get(url, headers=headers)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

