def intToRoman(num):
	"""
	:type num: int
	:rtype: str
	"""
	romanStr = ''
	romanStr += int(num / 1000) * 'M'
	num %= 1000

	if int(num / 100) == 9:
		romanStr += 'CM'
		num %= 100
	elif int(num / 100) == 4:
		romanStr += 'CD'
		num %= 100
	else:
		romanStr += int(num / 500) * 'D'
		num %= 500
		romanStr += int(num / 100) * 'C'
		num %= 100

	if int(num / 10) == 9:
		romanStr += 'XC'
		num %= 10
	elif int(num / 10) == 4:
		romanStr += 'XL'
		num %= 10
	else:
		romanStr += int(num / 50) * 'L'
		num %= 50
		romanStr += int(num / 10) * 'X'
		num %= 10

	if num == 9:
		romanStr += 'IX'
	elif num == 4:
		romanStr += 'IV'
	else:
		romanStr += int(num / 5) * 'V'
		num %= 5
		romanStr += num * 'I'

	return romanStr

	# if "IIII" in romanStr:
	# 	romanStr = romanStr.replace("IIII", 'IV')
	# 	# location = romanStr.find("IIII")
	# 	# if location != 0:
	# 	# 	romanStr = romanStr.replace("IIII", 'I')
	# 	# 	romanStr = list(romanStr)
	# 	# 	romanStr[location - 1], romanStr[location] = romanStr[location], romanStr[location - 1]
	# 	# 	romanStr = "".join(romanStr)
	# 	# else:
	# 	# 	romanStr = romanStr.replace("IIII", 'IV')
	# if "XXXX" in romanStr:
	# 	romanStr = romanStr.replace("XXXX", 'XL')
	# 	# location = romanStr.find("XXXX")
	# 	# if location != 0:
	# 	# 	romanStr = romanStr.replace("XXXX", 'X')
	# 	# 	romanStr = list(romanStr)
	# 	# 	romanStr[location - 1], romanStr[location] = romanStr[location], romanStr[location - 1]
	# 	# 	romanStr = "".join(romanStr)
	# 	# else:
	# 	# 	romanStr = romanStr.replace("XXXX", 'XL')
	# if "CCCC" in romanStr:
	# 	romanStr = romanStr.replace("CCCC", 'CD')
	# 	# location = romanStr.find("CCCC")
	# 	# if location != 0:
	# 	# 	romanStr = romanStr.replace("CCCC", 'C')
	# 	# 	romanStr = list(romanStr)
	# 	# 	romanStr[location - 1], romanStr[location] = romanStr[location], romanStr[location - 1]
	# 	# 	romanStr = "".join(romanStr)
	# 	# else:
	# 	# 	romanStr = romanStr.replace("CCCC", 'CD')

print(intToRoman(139))