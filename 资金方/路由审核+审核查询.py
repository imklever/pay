import time
import requests
import json


# fin = time.strftime("%Y%m%d%H%M%S", time.localtime())
# fund = fin + str(1)
loanAmount = [4000,60000]
loanTerm = [12,18]
repayMode = [3,4,5,6,9,10]
livingCity = [110100,120100]

# print (loanAmount)
# print (loanTerm)
# print (repayMode)
# print (livingCity)
# print(fin,fund)

url = 'http://fund.test.bkjk.cn/fund/api/exam/channelRouteExamine'
url1 = 'http://fund.test.bkjk.cn/fund/api/exam/channelRouteExamineQuery'
headers = {'Content-Type':'application/json'}

loanAmo = [4000,60000]
loanT = [12,18]
repayM = [3,4,5,6,9,10]
livingC = [110100,120100]

a=[]
for i in loanAmo:
	for y in loanT:
		for t in repayM:
			for r in livingC:
				a.append([i,y,t,r])

for b in range (len(a)):
	fin = time.strftime("%Y%m%d%H%M%S", time.localtime())
	fund = fin + str(1)
	# print (a[b][0],a[b][1],a[b][2],a[b][3],)
	loanAmount = a[b][0]
	loanTerm = a[b][1]
	repayMode = a[b][2]
	livingCity = a[b][3]

	print(loanAmount,loanTerm,repayMode,livingCity)



	data = {
		"productLine": "L_DECORATION_FINANCE",
		"productId":"ZXFQ20171111001",
		"productName":"装修贷",
		"financeOrderNo": fin,
		"fundLoanNo":fund,
		"loanApplyTime":"20180824094412123",
		"notifyUrl":"http://localhost:8280/fund/api/exam/xxxxx",
		"loanInfo":{
						"loanContractNo":fin,
						"loanAmount":loanAmount,
						"loanTerm":loanTerm,
						"termUnit":"MONTH",
						"signRate":0.6,
						"repayCycle":"0",
						"repayMode":repayMode
					},
		"borrowerInfo":{
						"borrowerName":"张四",
						"borrowerAge":30,
						"borrowerSex":"FEMALE",
						"telePhone":"17331791160",
						"idType":"ID_CARD",
						"idCardNo":"130984199009075161",
						"maritalStatus":"10",
						"livingCity":livingCity,
						"livingAddress":"110100",
						"postCode":"100020",
						"careerType":"8"
					}
	}
	ww = requests.post(url,data=json.dumps(data),headers=headers)
	# print(a.json())
	t = ww.json()
	# print(t)
	js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
	# print(js)

	time.sleep(0.5)

	data1 = {
		"financeOrderNo": fin,
		"fundLoanNo": fund
	}

	s1 = requests.post(url1, data=json.dumps(data1), headers=headers)
	t1 = s1.json()
	print('checkedChannelCode='+str(t1['checkedChannelCode']),'examStatus='+t1['examStatus'],'financeOrderNo='+t1['financeOrderNo'])
	# print('checkedChannelCode=%s,examStatus=%s,fin=%s' %(t1['checkedChannelCode'],t1['examStatus'],t1['fin']))
	# print()
	# print(t)
	js1 = json.dumps(t1, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)
	# print(js1)

	time.sleep(0.5)

	if str(livingCity) == '110100':
		if str(t1['checkedChannelCode']) == 'ZJF010':
			print('测试通过')

	print()
