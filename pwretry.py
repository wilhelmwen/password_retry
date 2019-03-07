x = 3
while x > 0:
	x = x - 1
	pw = input ('請輸入密碼: ')
	if pw == 'a123456':
		print('登入成功')
		break 
	else:
		print('密碼錯誤!')
		if x > 0:
			print('還有', x, '次機會')
		else:
			print('沒機會嘗試了! 要鎖帳號了啦!')
	

		
