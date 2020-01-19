
from typing import List

class Solution:
	def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
		ans = 0
		if len(points) <= 1:
			return ans
		for idx in range(1, len(points)):
			x1, y1 = points[idx - 1]
			x2, y2 = points[idx]
			x2, y2 = abs(x2 - x1), abs(y2 - y1)
			ans += (min(x2, y2) + abs(x2 - y2))
		return ans


print(Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
