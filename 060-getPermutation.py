from math import factorial
class Solution:
	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		ans = ""
		num = [str(i) for i in range(1, n + 1)]
		i = n - 1
		while len(ans) < n:
			if k % factorial(i) == 0:
				ans += num[k // factorial(i) - 1]
				num.pop(k // factorial(i) - 1)
				k %= factorial(i)
				i -= 1
			else:
				ans += num[k // factorial(i)]
				num.pop(k // factorial(i))
				k %= factorial(i)
				i = i - 1
		return ans

print(Solution().getPermutation(3, 6))