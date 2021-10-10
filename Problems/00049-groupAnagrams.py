def groupAnagrams(strs):
	"""
	:type strs: List[str]
	:rtype: List[List[str]]
	"""
	l = []
	sample = []
	for e in strs:
		if sorted(e) in sample:
			l[sample.index(sorted(e))].append(e)
		else:
			sample.append(sorted(e))
			l.append([e])
	return l
			

print(groupAnagrams(["eat", "eat"]))	