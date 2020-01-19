
from typing import List

class Solution:
	def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
		group = sorted([i for i in enumerate(groupSizes)], key = lambda x: x[1])
		ans, idx = [], 0
		while idx < len(group):
			currGroup, size = [], group[idx][1]
			for j in range(size):
				currGroup.append(group[idx][0])
				idx += 1
			ans.append(currGroup)
		return ans


print(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(Solution().groupThePeople([2, 1, 3, 3, 3, 2]))

