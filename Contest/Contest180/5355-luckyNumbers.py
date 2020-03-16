
from typing import List

class Solution:
	def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
		ans = []
		for i in range(len(matrix)):
			idx = matrix[i].index(min(matrix[i]))
			num = matrix[i][idx]
			col = [r[idx] for r in matrix]
			if num == max(col):
				ans.append(num)
		return ans

print(Solution().luckyNumbers([
	[3, 7, 8], 
	[9, 11, 13], 
	[15, 16, 17]
]))
