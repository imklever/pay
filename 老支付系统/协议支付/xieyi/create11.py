#coding:utf-8
import requests
from selenium import webdriver
import time
import json
import re


##创建协议入参
data = '{"transDesc":"聚合支付test1","businessId":"2","channelType":"LFT"}'
appid = '10005'
timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
key = 'EUZ9NunT9DQN+wg6p33vgw=='
s = appid+'&'+data+'&'+timestamp+'&'+key

############加密###################
driver = webdriver.Firefox()

u = 'http://tool.chinaz.com/tools/md5.aspx'
driver.get(u)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="q"]').send_keys(s)
driver.find_element_by_xpath('/html/body/div[3]/div/form/div/div[2]/div/input[1]').click()
time.sleep(3)
sign1 = driver.find_element_by_xpath('//*[@id="MD5Result"]').text
sign = sign1.lower()
print(sign)


#创建协议
url = 'http://172.29.66.21:80/api/protocol/create'
d = {'appId':appid, 'data':data,'sign':sign,'timestamp':timestamp}
print(d['data'])
data = json.dumps(d)
print(data)
headers ={"Content-Type":"application/json"}

s = requests.post(url,data=data,headers=headers)
print(s.status_code)
print(s.text)
sss = json.loads(s.text)

# print(sss)
# print(type(sss))
ss1 = sss['data']
ss = json.loads(ss1)
# print(ss)
# print(type(ss))
transNo = ss['transNo']
print('transNo:'+transNo,'amount:'+ss['amount'],'onpassageAmount:'+ss['onpassageAmount'],'outAmount:'+ss['outAmount'])


