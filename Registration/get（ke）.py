#coding:utf-8

import requests
import time
import json
import random

# no = time.strftime("%Y%m%d%H%M%S", time.localtime())

Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLmNvbSIsInNjb3BlIjpbImN1c3RvZGlhbi5yZWFkIiwiY3VzdG9kaWFuLndyaXRlIiwiYWR2aXNlLnJlYWQiLCJhZHZpc2Uud3JpdGUiLCJjaGFubmVsLnJlYWQiLCJjaGFubmVsLndyaXRlIiwibWVyY2hhbnQucmVhZCIsIm1lcmNoYW50LndyaXRlIiwicGF5bWVudC5yZWFkIiwicGF5bWVudC53cml0ZSIsImNsZWFyaW5nLnJlYWQiLCJjbGVhcmluZy53cml0ZSIsInJlY29uY2lsaWF0aW9uLnJlYWQiLCJyZWNvbmNpbGlhdGlvbi53cml0ZSIsIm9yZGVyLnJlYWQiLCJvcmRlci53cml0ZSJdLCJleHAiOjM2NzMyNTI5MTMsImF1dGhvcml0aWVzIjpbIlJPTEVfTUVSQ0hBTlRfQURNSU4iXSwianRpIjoiYWY1MzQ0MWYtMTVhYS00NmU4LWIwMzktN2Y0MGNlZTllNWEzIiwiY2xpZW50X2lkIjoic2ltdWxhdG9yIn0.yZmCQz_jumD0JzIC0TQ1Snnw2AzrRJnM-Sln65Cy6hg'
url = 'http://archimonde.dev.bkjk.cn/archimonde/api/merchants/events'
headers ={"Authorization":Authorization,"Content-Type":"application/json","Accept":'application/json'}
data = {"merchantId":"20180810175351224557"}

s = requests.get(url, params=data, headers=headers)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


