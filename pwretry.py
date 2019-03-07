x = 3
while x != 0:
	pw = input ('請輸入密碼: ')
	if pw == 'a123456':
		print('登入成功')
		break 
	else:
		x = x -1
		if x == 0:
			break
		print('密碼錯誤! 還有', x, '次機會')


	

		
