
from typing import List

class Solution:
	def minSubsequence(self, nums: List[int]) -> List[int]:
		nums = sorted(nums, reverse = True)
		s = sum(nums) - nums[0]
		s2 = nums[0]
		lst = [nums[0]]
		for i in range(1, len(nums)):
			if s2 > s:
				break
			else:
				s2 += nums[i]
				lst.append(nums[i])
				s -= nums[i]
		return lst

print(Solution().minSubsequence([4, 3, 10, 9, 8]))
print(Solution().minSubsequence([4, 4, 7, 6, 7]))
print(Solution().minSubsequence([6]))
