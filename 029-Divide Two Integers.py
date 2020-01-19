def divide(dividend, divisor):
	"""
	:type dividend: int
	:type divisor: int
	:rtype: int
	"""
	quotient = dividend // divisor
	if quotient < 0 and dividend % divisor != 0:
		quotient += 1
	if quotient > 2 ** 31 - 1:
		return 2 ** 31 - 1
	elif quotient < -(2 ** 31):
		return -(2 ** 31)
	return quotient