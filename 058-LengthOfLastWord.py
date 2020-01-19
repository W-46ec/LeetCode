def lengthOfLastWord(s):
	"""
	:type s: str
	:rtype: int
	"""
	if len(s.replace(' ', '')) == 0:
		return 0
	i = -1
	length = len(s.split(' ')[i])
	while length == 0:
		i -= 1
		length = len(s.split(' ')[i])
	return length

print(lengthOfLastWord('  H '))