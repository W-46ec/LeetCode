class Solution:
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = 1
		while n in nums:
			n += 1
		return n

print(Solution().firstMissingPositive([3, 4, -1, 1]))