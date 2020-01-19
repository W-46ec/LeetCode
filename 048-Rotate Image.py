def rotate(matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: void Do not return anything, modify matrix in-place instead.
	"""
	n = len(matrix)
	if n > 0:
		for i in range(n):
			for j in range(i + 1, n):
				t = matrix[i][j]
				matrix[i][j] = matrix[j][i]
				matrix[j][i] = t
		for i in matrix:
			i.reverse()

rotate([[1,2,3],[4,5,6],[7,8,9]])