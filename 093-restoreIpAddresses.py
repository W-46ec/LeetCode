class Solution:
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		ans = []
		if len(s) > 12:
			return ans
		for i in range(1, len(s)):
			if s[0: i] == '' or (len(s[0: i]) > 1 and s[0] == '0'):
				break
			for j in range(i + 1, len(s)):
				if s[i: j] == '' or (len(s[i: j]) > 1 and s[i] == '0'):
					break
				for k in range(j + 1, len(s)):
					if s[j: k] == '' or (len(s[j: k]) > 1 and s[j] == '0'):
						break
					elif len(s[k: len(s)]) > 1 and s[k] == '0':
						continue
					if int(s[0: i]) <= 255 and \
						int(s[i: j]) <= 255 and \
						int(s[j: k]) <= 255 and \
						int(s[k: len(s)]) <= 255:
						ans.append(
							s[0: i] + '.' + 
							s[i: j] + '.' + 
							s[j: k] + '.' + 
							s[k: len(s)]
						)
		return ans


print(Solution().restoreIpAddresses("010010"))
print(Solution().restoreIpAddresses("0000"))
print(Solution().restoreIpAddresses("101023"))