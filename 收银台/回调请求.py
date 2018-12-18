#coding:utf-8

import requests
import time
import json
import random
import var
import re


url = 'https://payment.dev.bkjk-inc.com/deepfury/api/envelopes'
headers ={"Content-Type":"application/json"}
data = {"no":"201812031123561","ownerId":"OLDAMAN"}


s = requests.get(url, headers=headers,params=data)
print(s.status_code)
t = s.json()
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
