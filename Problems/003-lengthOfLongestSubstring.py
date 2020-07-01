def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""

	stringList = []
	if s == "":
		return 0
	for i in range(0, len(s)):
		tmp = s[i]
		for j in range(i + 1, len(s)):
			if s[j] not in tmp:
				tmp += s[j]
			else:
				break
		stringList.append(tmp)

	stringList = sorted(stringList, key = len)
	return len(stringList[-1])

print(lengthOfLongestSubstring("pwwkew"))
