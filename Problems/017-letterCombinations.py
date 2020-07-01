def letterCombinations(digits):
	"""
	:type digits: str
	:rtype: List[str]
	"""
	table = {
		'1': '', 
		'2': 'abc', 
		'3': 'def', 
		'4': 'ghi', 
		'5': 'jkl', 
		'6': 'mno', 
		'7': 'pqrs', 
		'8': 'tuv', 
		'9': 'wxyz'
	}
	if len(digits) == 0:
		return []
	elif len(digits) == 1:
		return list(table[digits[0]])
	combinations = []
	for d in range(len(digits)):
		if d != '1':
			if len(combinations) == 0:
				combinations = list(table[digits[d]])
			else:
				current = []
				for i in combinations:
					current.extend(list(map(lambda c: i + c, [x for x in table[digits[d]]])))
					combinations = current
	return combinations


print(letterCombinations("23"))