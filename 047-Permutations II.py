class Solution:
	def permuteUnique(self, nums):
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
			answer.append([nums[0], nums[1]])
			if [nums[1], nums[0]] not in answer:
				answer.append([nums[1], nums[0]])
			return answer
		else:
			for i in nums:
				l = nums.copy()
				l.remove(i)
				for j in self.permuteUnique(l):
					j.append(i)
					if j not in answer:
						answer.append(j)
		return answer

print(Solution().permute([-1, -1, 0]))