def myAtoi(str):
	"""
	:type str: str
	:rtype: int
	"""
	if len(str) == 0:
		return 0
	s = ''
	isFirst = True
	for c in str:
		if isFirst:
			if c in "-+0123456789":
				s += c
				isFirst = False
			elif c != ' ':
				return 0
		else:
			if c in "0123456789":
				s += c
			else:
				break
	if len(s) == 0:
		return 0

	sign = 1
	if s[0] == '-':
		sign = -1
		s = s[1:]
	elif s[0] == '+':
		s = s[1:]
	if len(s) == 0:
		return 0
	num = int(s) * sign
	if num <= -(2 ** 31):
		return -(2 ** 31)
	elif num >= 2 ** 31 - 1:
		return 2 ** 31 - 1
	else:
		return num

print(myAtoi('   -23 44'))