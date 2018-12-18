#coding:utf-8

def LuYou(area,money,period,way):
    if (area == '北京'):
        if (way in [1,2,3,4,5,6,9,10,11,12]):
            return '通道A'
        else:
            return '无可用通道'
    elif money <= 30 * 10000:
        if ((money > 20 * 10000) or (money < 1000)) and (period == 12) and (way in [1,2,3,9]):
            return '通道B'
        elif ((money <= 20 * 10000) and (money >= 1000)):
            if (period == 12) and (way in [3,9]):
                return '通道B'
            elif (period == 12) and (way in [1,2]):
                return '通道B or 通道C'
            elif (period in [18,24,36]) and (way in [4,5,10,11,12]):
                return '通道C'
            else:
                return '无可用通道'
        else:
            return '无可用通道'
    else:
        return '无可用通道'


t = LuYou('q',10000,12,1)
print(t)




def LuYou1(area,money,period,way):
    if (area == '北京'):
        if (way in [1,2,3,4,5,6,9,10,11,12]):
            return '通道A'
        else:
            return '无可用通道'
    elif money <= 30 * 10000:
        if ((money <= 20 * 10000) and (money >= 1000)):
            if (period == 12):
                if (way in [1,2]):
                    return '通道B or 通道C'
                elif (way in [4,5,10,11,12]):
                    return '通道C'
                elif (way in [3,9]):
                    return '通道B'
                else:
                    return '无可用通道'
            elif (period in [18,24,36]):
                if (way in [1,2,4,5,10,11,12]):  ####3
                    return '通道C'
                else:
                    return '无可用通道'
            else:
                return '无可用通道'
        elif (period == 12) and (way in [1,2,3,9]):
            return '通道B'
        else:
            return '无可用通道'
    else:
        return '无可用通道'


t1 = LuYou1('q',10000,12,1)
print(t1)