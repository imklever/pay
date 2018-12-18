#coding:utf-8

import hashlib

############加密###################
def md5(s):
    md5 = hashlib.md5()
    sign_bytes_utf8 = s.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    sign = md5.hexdigest()
    print('加密结果：'+sign)
    return sign

