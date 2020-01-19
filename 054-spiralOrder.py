class Solution:
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if len(matrix) == 0:
			return []
		ans = []
		steps = []
		directions = ['R', 'D', 'L', 'U']
		m, n = len(matrix), len(matrix[0])
		while m > 0 and n > 0:
			steps.append(n)
			n -= 1
			m -= 1
			if m > 0:
				steps.append(m)
		x, y = 0, -1
		for i in range(len(steps)):
			for j in range(steps[i]):
				if directions[i % 4] == 'R':
					y += 1
				elif directions[i % 4] == 'D':
					x += 1
				elif directions[i % 4] == 'L':
					y -= 1
				elif directions[i % 4] == 'U':
					x -= 1
				ans.append(matrix[x][y])
		return ans

print(Solution().spiralOrder(
		[
			[1, 2, 3, 4, 5], 
			[6, 7, 8, 9, 10], 
			[11, 12, 13, 14, 15]
		]
	)
)