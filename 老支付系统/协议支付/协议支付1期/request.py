#coding:utf-8
import json
import random

import requests

import jiami
import time

#公用参数
appid = '10005'
key = 'EUZ9NunT9DQN+wg6p33vgw=='
num = random.randint(100,999)

def request(url,data):
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(num)
    print(timestamp)
    s = appid + '&' + json.dumps(data) + '&' + timestamp + '&' + key
    print('加密报文：' + s)

    sign = jiami.md5(s)

    d = {'appId':appid, 'data':json.dumps(data),'sign':sign,'timestamp':timestamp}
    print('入参data：'+d['data'])
    data = json.dumps(d)
    print('请求报文：'+data)
    headers ={"Content-Type":"application/json"}

    s = requests.post(url,data=data,headers=headers)
    print('接口状态：'+str(s.status_code))
    print('返回报文：'+s.text)
    return s.text


def request1(url,data):
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(num)
    print(timestamp)
    s = appid + '&' + data + '&' + timestamp + '&' + key
    print('加密报文：' + s)

    sign = jiami.md5(s)

    d = {'appId':appid, 'data':data,'sign':sign,'timestamp':timestamp}
    print('入参data：'+d['data'])
    data = json.dumps(d)
    print('请求报文：'+data)
    headers ={"Content-Type":"application/json"}

    s = requests.post(url,data=data,headers=headers)
    print('接口状态：'+str(s.status_code))
    print('返回报文：'+s.text)
    return s.text
