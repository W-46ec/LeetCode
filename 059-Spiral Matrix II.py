class Solution:
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		l = []
		steps = []
		directions = ['R', 'D', 'L', 'U']
		for i in range(n):
			l.append([0] * n)
		steps.append(n)
		for i in range(n - 1, 0, -1):
			steps.append(i)
			steps.append(i)

		num = 1
		x, y = 0, -1
		for idx in range(len(steps)):
			for i in range(steps[idx]):
				if directions[idx % 4] == 'R':
					y += 1
				elif directions[idx % 4] == 'D':
					x += 1
				elif directions[idx % 4] == 'L':
					y -= 1
				elif directions[idx % 4] == 'U':
					x -= 1
				l[x][y] = num
				num += 1
		return l

n = 5
l = Solution().generateMatrix(n)
for i in range(n):
	print(l[i])