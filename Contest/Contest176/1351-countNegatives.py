
from typing import List

class Solution:
	def countNegatives(self, grid: List[List[int]]) -> int:
		ans = 0
		for row in grid:
			ans += len(list(filter(lambda x: x < 0, row)))
		return ans

print(Solution().countNegatives([
	[4, 3, 2, -1], 
	[3, 2, 1, -1], 
	[1, 1, -1, -2], 
	[-1, -1, -2, -3]
]))
