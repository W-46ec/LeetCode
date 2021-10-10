class Solution:
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		ans = []
		nums = [i for i in range(1, n + 1)]
		def combination(U, subset, targetLength):
			if len(subset) == targetLength:
				ans.append(subset)
			elif len(subset) > targetLength:
				return
			else:
				if len(subset) != 0:
					idx = U.index(subset[-1])
				else:
					idx = -1
				for i in range(idx + 1, len(U)):
					combination(U, subset + [U[i]], targetLength)
		combination(nums, [], k)
		return ans

print(Solution().combine(4, 3))