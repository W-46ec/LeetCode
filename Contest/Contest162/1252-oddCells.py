
from typing import List

class Solution:
	def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
		matrix = [[0] * m for i in range(n)]
		for idx in indices:
			matrix[idx[0]] = list(map(lambda x: x + 1, matrix[idx[0]]))
			for j in range(n):
				matrix[j][idx[1]] += 1
		return sum([1 for row in matrix for x in row if x % 2 == 1])

print(Solution().oddCells(2, 3, [[0, 1], [1, 1]]))

