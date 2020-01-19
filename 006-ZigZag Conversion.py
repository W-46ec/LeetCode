def convert(s, numRows):
	"""
	:type s: str
	:type numRows: int
	:rtype: str
	"""
	
	if numRows == 1:
		return s

	converted = []

	for i in range(0, numRows):
		converted.append([])

	direction = 'down'
	j = -1
	for i in s:
		if direction == 'down':
			j += 1
			converted[j].append(i)
			if j == numRows - 1:
				direction = 'up'
		elif direction == 'up':
			j -= 1
			converted[j].append(i)
			if j == 0:
				direction = 'down'
	string = ''
	for i in converted:
		string += "".join(i)
	return string

print(convert("1234567890", 3))