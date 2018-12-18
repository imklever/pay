#coding:utf-8
import requests
from selenium import webdriver
import time
import json
import re


#公用参数
appid = '10005'
key = 'EUZ9NunT9DQN+wg6p33vgw=='


############加密###################
def jiami(s):
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

    driver.close()

    return sign



# ##创建协议入参
# data1 = '{"transDesc":"聚合支付test1","businessId":"2","channelType":"LFT"}'
# timestamp1 = time.strftime("%Y%m%d%H%M%S", time.localtime())
# s1 = appid+'&'+data1+'&'+timestamp1+'&'+key

# sign1 = jiami(s1)

# #创建协议
# url1 = 'http://172.29.66.21:80/api/protocol/create'
# d1 = {'appId':appid, 'data':data1,'sign':sign,'timestamp':timestamp1}
# print(d1['data'])
# data11 = json.dumps(d1)
# print(data11)
# headers ={"Content-Type":"application/json"}
#
# s1 = requests.post(url1,data=data11,headers=headers)
# print(s1.status_code)
# print(s1.text)
# sss1 = json.loads(s1.text)
#
# # print(sss)
# # print(type(sss))
# ss11 = sss1['data']
# ss1 = json.loads(ss11)
# # print(ss)
# # print(type(ss))
# transNo = ss1['transNo']
# print('transNo:'+transNo,'amount:'+ss1['amount'],'onpassageAmount:'+ss1['onpassageAmount'],'outAmount:'+ss1['outAmount'])


transNo = 'TR180710155909152480137'

##查询协议入参
data2 = {"transNo":transNo}
timestamp2 = time.strftime("%Y%m%d%H%M%S", time.localtime())
s2 = appid+'&'+json.dumps(data2)+'&'+timestamp2+'&'+key
print(s2)

#加密
sign2 = jiami(s2)

#查询协议
url2 = 'http://172.29.66.21:80/api/protocol/find'
d2 = {'appId':appid, 'data':json.dumps(data2),'sign':sign2,'timestamp':timestamp2}
print(d2['data'])
data21 = json.dumps(d2)
print(data21)
headers ={"Content-Type":"application/json"}

s2 = requests.post(url2,data=data21,headers=headers)
print(s2.status_code)
print(s2.text)
sss2 = json.loads(s2.text)

# print(sss)
# print(type(sss))
ss21 = sss2['data']
ss2 = json.loads(ss21)
# print(ss)
# print(type(ss))
transNo = ss2['transNo']
print('transNo:'+transNo,'amount:'+ss2['amount'],'onpassageAmount:'+ss2['onpassageAmount'],'outAmount:'+ss2['outAmount'])
