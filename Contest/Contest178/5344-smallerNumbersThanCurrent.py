
from typing import List

class Solution:
	def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
		lst = sorted(nums)
		ans = []
		for i in nums:
			ans.append(lst.index(i))
		return ans

print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(Solution().smallerNumbersThanCurrent([6, 5, 4, 8]))
print(Solution().smallerNumbersThanCurrent([7, 7, 7, 7]))
