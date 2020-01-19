
from typing import List

class Solution:
	def minTaps(self, n: int, ranges: List[int]) -> int:
		coverage = []
		for i in enumerate(ranges):
			coverage.append([i[0] - i[1], i[0] + i[1]])
		coverage = sorted(coverage, key = lambda x: x[1] - x[0], reverse = True)
		print(coverage)
		idx = 0
		while idx < len(coverage):
			idx2 = idx + 1
			while idx2 < len(coverage):
				if coverage[idx2][0] >= coverage[idx][0] and \
					coverage[idx2][1] <= coverage[idx][1]:
					coverage.pop(idx2)
					continue
				idx2 += 1
			idx += 1
		coverage = sorted(coverage)
		print(coverage)
		if len(coverage) == 1:
			return 1 if coverage[0][0] <= 0 and coverage[0][1] >= n else -1
		idx = 0
		while idx < len(coverage) - 1:
			if coverage[idx + 1][0] > coverage[idx][1]:
				return -1
			idx += 1
		idx = 1
		while idx < len(coverage) - 2:
			if coverage[idx - 1][1] >= coverage[idx + 1][0]:
				coverage.pop(idx)
				continue
			idx += 1
		print(coverage)
		idx, count = 0, len(coverage)
		left, right = False, False
		while idx < len(coverage) - 1:
			if coverage[idx][0] <= 0:
				left = True
			if coverage[idx][1] >= n:
				right = True
			if coverage[idx + 1][0] <= 0:
				count -= 1
			elif coverage[idx + 1][0] >= n:
				count -= 1
			else:
				if left and right:
					count -= 1
			idx += 1
		return count


# print(Solution().minTaps(5, [3, 4, 1, 1, 0, 0]))
# print(Solution().minTaps(3, [0, 0, 0]))
# print(Solution().minTaps(7, [1, 2, 1, 0, 2, 1, 0, 1]))
# print(Solution().minTaps(8, [4, 0, 0, 0, 0, 0, 0, 0, 4]))
# print(Solution().minTaps(8, [4, 0, 0, 0, 4, 0, 0, 0, 4]))
# print(Solution().minTaps(17, [0, 3, 3, 2, 2, 4, 2, 1, 5, 1, 0, 1, 2, 3, 0, 3, 1, 1]))

# Expected 4
print(Solution().minTaps(25, [3,0,1,5,4,1,4,2,4,4,3,3,3,0,3,2,5,1,5,5,2,3,1,0,2,4]))

