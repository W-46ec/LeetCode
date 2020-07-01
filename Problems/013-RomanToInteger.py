def romanToInt(s):
	"""
	:type s: str
	:rtype: int
	"""
	currentSignificance = 0
	length = len(s)
	l = list(s)
	sumOfRoman = 0

	significanceTable = {
		'I': 0, 
		'V': 1, 
		'X': 2, 
		'L': 3, 
		'C': 4, 
		'D': 5, 
		'M': 6
	}

	symbolTable = {
		'I': 1, 
		'V': 5, 
		'X': 10, 
		'L': 50, 
		'C': 100, 
		'D': 500, 
		'M': 1000
	}

	while length > 0:
		if significanceTable[l[length - 1]] >= currentSignificance:
			sumOfRoman += symbolTable[l[length - 1]]
			currentSignificance = significanceTable[l[length - 1]]
		else:
			sumOfRoman -= symbolTable[l[length - 1]]
		length -= 1

	return sumOfRoman

print(romanToInt("II"))