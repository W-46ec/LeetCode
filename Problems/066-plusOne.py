def plusOne(digits):
	"""
	:type digits: List[int]
	:rtype: List[int]
	"""
	return list(map(int, list(str(int("".join(list(map(str, digits)))) + 1))))

print(plusOne([9, 9, 9]))