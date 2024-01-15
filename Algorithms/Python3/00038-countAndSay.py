def countAndSay(n):
	"""
	:type n: int
	:rtype: str
	"""
	say = '1'
	nextStr = ''
	while n > 1:
		location = 0
		while location < len(say):
			count = 0
			while location + count < len(say):
				if say[location + count] == say[location]:
					count += 1
				else:
					break
			nextStr += str(count) + say[location]
			location += count
		say = nextStr
		nextStr = ''
		n -= 1
	return say

print(countAndSay(6))