#coding:utf-8
from selenium import webdriver
import time
import hashlib

#公用参数
appid = '10005'
key = 'EUZ9NunT9DQN+wg6p33vgw=='


############网页加密###################
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


############md5程序加密###################
def md5(s):
    md5 = hashlib.md5()
    sign_bytes_utf8 = s.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    sign = md5.hexdigest()
    print('加密结果：'+sign)
    return sign