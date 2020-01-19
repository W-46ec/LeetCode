class Solution:
	def factorial(self, n):
		if n <= 0:
			return 1
		else:
			return n == 1 or n * self.factorial(n - 1)

	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 0:
			return 0
		s = 0
		for i in range(n // 2 + 1):
			s += int(self.factorial(n - i) / (self.factorial(i) * self.factorial(n - 2 * i)))
		return s

print(Solution().climbStairs(0))


# import math

# class Solution:
# 	def climbStairs(self, n):
# 		"""
# 		:type n: int
# 		:rtype: int
# 		"""
# 		if n <= 0:
# 			return 0
# 		s = 0
# 		for i in range(n // 2 + 1):
# 			s += int(math.factorial(n - i) / (math.factorial(i) * math.factorial(n - 2 * i)))
# 		return s