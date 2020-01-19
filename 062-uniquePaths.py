import math
class Solution:
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		return int(math.factorial(m - 1 + n - 1) / (math.factorial(m - 1) * math.factorial(n - 1)))

print(Solution().uniquePaths(7, 3))