
from typing import List

class Solution:
	def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
		empty, matrix = [], [[0] * len(colsum) for i in range(2)]
		ones = [e for e in enumerate(colsum) if e[1] == 1]
		twos = [e for e in enumerate(colsum) if e[1] == 2]
		for i in twos:
			matrix[0][i[0]] = matrix[1][i[0]] = 1
		upper -= len(twos)
		lower -= len(twos)
		if upper < 0 or lower < 0 \
			or upper + lower != len(ones):
			return []
		else:
			for i in ones:
				if upper:
					matrix[0][i[0]] = 1
					upper -= 1
				else:
					if lower <= 0:
						return []
					matrix[1][i[0]] = 1
					lower -= 1
		return matrix

print(Solution().reconstructMatrix(5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]))

