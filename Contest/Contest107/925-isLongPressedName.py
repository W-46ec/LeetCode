class Solution:
	def isLongPressedName(self, name, typed):
		"""
		:type name: str
		:type typed: str
		:rtype: bool
		"""
		if name == typed:
			return True
		l1 = list(name)
		l2 = list(typed)
		while len(l1) > 0 and len(l2) > 0:
			if l1[0] != l2[0]:
				return False
			s1 = "" + l1.pop(0)
			while len(l1) > 0 and l1[0] == s1[0]:
				s1 += l1.pop(0)
			s2 = "" + l2.pop(0)
			while len(l2) > 0 and l2[0] == s2[0]:
				s2 += l2.pop(0)
			if len(s1) > len(s2):
				return False
		if len(l1) > 0:
			return False
		return True
		# idx1, idx2 = 0, 1
		# while idx2 < len(name):
		# 	if name[idx1] not in typed:
		# 		return False
		# 	while idx2 < len(name) and name[idx2] == name[idx1]:
		# 		idx2 += 1
		# 	if idx2 != idx1 + 1:
		# 		if name[idx1 : idx2 + 1] not in typed:
		# 			return False
		# 	idx1 += 1
		# 	idx2 += 1
		# return True
print(Solution().isLongPressedName("pyplrz", "ppyypllr"))