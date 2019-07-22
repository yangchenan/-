password = '123456'
count = 3
while count > 0:
	count = count-1
	guess = input('請輸入密碼:')
	if guess != password:
		print('輸入錯誤,你還有', count, '次機會')
	else :
		print('答對囉!')	
		break

