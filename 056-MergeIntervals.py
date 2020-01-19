
from typing import List

class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		intervals = sorted(intervals)
		if len(intervals) <= 1:
			return intervals
		i, length = 0, len(intervals)
		while i < length - 1:
			itvl1, itvl2 = intervals[i], intervals[i + 1]
			if itvl2[0] <= itvl1[1]:
				if itvl2[1] <= itvl1[1]:
					intervals.pop(i + 1)
				else:
					intervals[i + 1] = [itvl1[0], itvl2[1]]
					intervals.pop(i)
				length -= 1
				continue
			i += 1
		return intervals

print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [4, 5]]))
print(Solution().merge([[1, 4], [2, 3]]))

