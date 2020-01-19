class Solution:
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = sorted(nums)
		if nums[0] != 0:
			return 0
		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1] + 1:
				return i
		return len(nums)

print(Solution().missingNumber([0, 3, 1]))
print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(Solution().missingNumber([0, 1, 2, 3]))