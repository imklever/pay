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
    print('加密结果：'+sign)

    driver.close()

    return sign


def request(url,data):
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    s = appid + '&' + json.dumps(data) + '&' + timestamp + '&' + key
    print('加密报文：' + s)

    sign = jiami(s)

    d = {'appId':appid, 'data':json.dumps(data),'sign':sign,'timestamp':timestamp}
    print('data:'+d['data'])
    data = json.dumps(d)
    print('请求报文：'+data)
    headers ={"Content-Type":"application/json"}

    s = requests.post(url,data=data,headers=headers)
    print('接口状态：'+str(s.status_code))
    print('返回报文：'+s.text)
    return s.text


##创建协议入参
data1 = {"transDesc":"test1","businessId":"2","channelType":"LFT"}
#创建协议请求地址
url1 = 'http://172.29.66.21:80/api/protocol/create'

t1 = request(url1,data1)

sss1 = json.loads(t1)
ss11 = sss1['data']
ss1 = json.loads(ss11)
transNo = ss1['transNo']
print('transNo:'+transNo,'amount:'+ss1['amount'],'onpassageAmount:'+ss1['onpassageAmount'],'outAmount:'+ss1['outAmount'])

print('####################创建协议结束##################')

##查询协议入参
data2 = {"transNo":transNo}
#查询协议请求地址
url2 = 'http://172.29.66.21:80/api/protocol/find'

t2 = request(url2,data2)

sss2 = json.loads(t2)
ss21 = sss2['data']
ss2 = json.loads(ss21)
print('transNo:'+transNo,'amount:'+ss2['amount'],'onpassageAmount:'+ss2['onpassageAmount'],'outAmount:'+ss2['outAmount'])

print('####################查询协议结束##################')
