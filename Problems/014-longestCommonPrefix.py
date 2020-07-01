def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""

	prefix = ''
	shortest = ''

	if len(strs) > 0:
		shortest = strs[0]
	else:
		return ''
	for e in strs:
		if len(e) < len(shortest):
			shortest = e

	for i in range(0, len(shortest)):
		commonPrefix = True
		for c in strs:
			if c[i] != shortest[i]:
				commonPrefix = False
		if commonPrefix:
			prefix += shortest[i]
		else:
			break

	return prefix


print(longestCommonPrefix(['aca', 'cba']))