password = 'a123456'
x = 0
while True:
	p = input('請輸入密碼：')
	x = x + 1
	if p == password:
		print('登入成功！')
		break
	elif x == 1:
		print('密碼錯誤！還有2次機會')
	elif x == 2:
		print('密碼錯誤！還有1次機會')
	elif x >= 3:
		print('密碼錯誤！')
		break
