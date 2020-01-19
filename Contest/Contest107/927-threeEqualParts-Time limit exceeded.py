class Solution:
	def binToDec(self, s):
		if len(s) != 0:
			return int(s, base = 2)
		else:
			return 0
	def threeEqualParts(self, A):
		"""
		:type A: List[int]
		:rtype: List[int]
		"""
		ans = [-1, -1]
		string = "".join([str(i) for i in A])
		i, j = 0, 1
		for i in range(len(string)):
			for j in range(i + 1, len(string)):
				a = self.binToDec(string[: i + 1])
				b = self.binToDec(string[i + 1 : j + 1])
				c = self.binToDec(string[j + 1:])
				if a == b and b == c:
					return [i, j + 1]
		return ans

# print(Solution().threeEqualParts([1, 0, 1, 0, 1]))
print(Solution().threeEqualParts([1, 1, 0, 1, 1]))