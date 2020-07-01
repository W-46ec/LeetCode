class Solution:
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		ans = []
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
		for i in range(len(nums) + 1):
			if i == 0:
				ans.append([])
				continue
			combination(nums, [], i)
		return ans

print(Solution().subsets([1, 2, 3]))