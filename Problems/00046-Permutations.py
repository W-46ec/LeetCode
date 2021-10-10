class Solution:
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if len(nums) == 0:
			return []
		elif len(nums) == 1:
			return [nums]

		answer = []

		if len(nums) == 2:
			return [
				[nums[0], nums[1]], 
				[nums[1], nums[0]]
			]
		else:
			for i in nums:
				l = nums.copy()
				l.remove(i)
				for j in self.permute(l):
					j.append(i)
					answer.append(j)
		return answer

print(Solution().permute([1, -1, 0]))