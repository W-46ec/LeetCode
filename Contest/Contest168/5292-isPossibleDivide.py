
from typing import List

class Solution:
	def isPossibleDivide(self, nums: List[int], k: int) -> bool:
		if len(nums) % k != 0:
			return False
		nums = sorted(nums)
		Q = []
		while len(nums) != 0:
			if len(Q) == 0:
				Q.append(nums.pop(0))
			ele = Q.pop(0)
			while len(nums) > 0 and nums[0] == ele:
				Q.append(nums.pop(0))
			idx, count = 0, 1
			while count < k:
				if len(nums) <= 0 or idx >= len(nums):
					return False
				elif nums[idx] == ele + 1:
					ele = nums.pop(idx)
					count += 1
					idx -= 1
				else:
					idx += 1
		return True

print(Solution().isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4))
print(Solution().isPossibleDivide([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
print(Solution().isPossibleDivide([3, 3, 2, 2, 1, 1], 3))
print(Solution().isPossibleDivide([1, 2, 3, 4], 3))
