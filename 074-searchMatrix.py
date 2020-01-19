class Solution:
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if len(matrix) == 0:
			return False
		elif len(matrix[0]) == 0:
			return False
		row, col = len(matrix), len(matrix[0])
		l, r = 0, row * col - 1
		while l <= r:
			middle = (l + r) // 2
			if matrix[middle // col][middle % col] > target:
				r = middle - 1
			elif matrix[middle // col][middle % col] < target:
				l = middle + 1
			else:
				return True
		return False

print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 13))