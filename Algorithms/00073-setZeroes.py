class Solution:
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		row, col = [], []
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if matrix[i][j] == 0:
					if i not in row:
						row.append(i)
					if j not in col:
						col.append(j)
		for i in row:
			matrix[i] = [0] * len(matrix[i])
		for j in col:
			for i in range(len(matrix)):
				matrix[i][j] = 0

matrix = [
	[0,1,2,0],
	[3,4,5,2],
	[1,3,1,5]
]
Solution().setZeroes(matrix)
print(matrix)