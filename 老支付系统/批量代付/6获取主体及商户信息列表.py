#coding:utf-8

'''
代付绑卡
https://payment.test.bkjk.com/dfapi/mechantinfos

        "中易购（北京）金融服务外包有限公司":"2",
        "广州亿达按揭服务有限公司":"40",
        "中易购金融服务外包有限公司(作废，不再使用)":"6",
        "中易购（北京）金融服务外包有限公司南京分公司":"10",
        "中津国汇（天津）服务外包有限公司":"4",
        "湖南佳平商业信息咨询有限公司":"16",
        "沈阳中晟卓越信息技术有限公司":"7",
        "武汉大恒融金商业信息咨询有限公司":"15",
        "济南晅鼎金融软件服务有限公司":"8",
        "厦门中金聚鑫金融信息服务有限公司":"12",
        "杭州国实资产管理有限公司":"13",
        "成都瑞盈添富金融服务外包有限公司":"17",
        "中腾卓越（青岛）金融服务有限公司":"9",
        "北京中融信融资担保有限公司":"1",
        "苏州安佳信息科技有限公司":"42",
        "中金华融（深圳）金融服务有限公司":"18",
        "合肥融贝科技有限公司":"11",
        "大连鸿拓企业管理服务有限公司":"5",
        "北京美锦互联网金融信息有限公司":"3"
'''
#coding:utf-8
import requests
import json
import random
import time

url = 'https://payment.test.bkjk.com/dfapi/mechantinfos'
headers ={"Content-Type":"application/json"}

s = requests.post(url, headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

