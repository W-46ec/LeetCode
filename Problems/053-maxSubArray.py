class Solution:
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return None
		currentMax = nums[0]
		currentSum = nums[0]
		for i in range(1, len(nums)):
			if currentSum < 0:
				currentSum = nums[i]
			else:
				# The purpose of this part is to select the part that can sum up to 0
				# num[i] may make contribution, or not
				# Anyway, we will choose the maximum one out of those possible outcomes
				currentSum += nums[i]
			currentMax = max(currentMax, currentSum)
		return currentMax

print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))