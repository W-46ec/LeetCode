class Solution:
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		num0, num1 = nums.count(0), nums.count(1)
		num2 = len(nums) - num0 - num1
		idx = 0
		for i in range(num0):
			nums[idx] = 0
			idx += 1
		for i in range(num1):
			nums[idx] = 1
			idx += 1
		for i in range(num2):
			nums[idx] = 2
			idx += 1
		

nums = [2, 0, 2, 1, 1, 0]
print(nums)
Solution().sortColors(nums)
print(nums)