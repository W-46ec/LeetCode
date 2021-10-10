class Solution:
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		return int(x ** (1 / 2))

print(Solution().mySqrt(8))