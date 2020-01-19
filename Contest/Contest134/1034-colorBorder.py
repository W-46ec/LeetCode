class Solution:
	def colorBorder(self, grid: 'List[List[int]]', r0: 'int', c0: 'int', color: 'int') -> 'List[List[int]]':
		row, column = len(grid), len(grid[0])
		border, visited = [[False] * column for i in range(row)], [[False] * column for i in range(row)]
		Q = []
		initColor = grid[r0][c0]

		Q.append((r0, c0))
		idx = 0
		while idx < len(Q):
			isInside = True
			x, y = Q[idx][0], Q[idx][1]
			visited[x][y] = True
			if x + 1 < row:
				if visited[x + 1][y] == False:
					if grid[x + 1][y] == initColor:
						Q.append((x + 1, y))
					else:
						border[x][y] = True
						isInside = False
			else:
				border[x][y] = True

			if x - 1 >= 0:
				if visited[x - 1][y] == False:
					if grid[x - 1][y] == initColor:
						Q.append((x - 1, y))
					else:
						border[x][y] = True
						isInside = False
			else:
				border[x][y] = True

			if y + 1 < column:
				if visited[x][y + 1] == False:
					if grid[x][y + 1] == initColor:
						Q.append((x, y + 1))
					else:
						border[x][y] = True
						isInside = False
			else:
				border[x][y] = True

			if y - 1 >= 0:
				if visited[x][y - 1] == False:
					if grid[x][y - 1] == initColor:
						Q.append((x, y - 1))
					else:
						border[x][y] = True
						isInside = False
			else:
				border[x][y] = True

			if isInside == False:
				border[x][y] = True
			idx += 1

		for i in range(row):
			for j in range(column):
				if border[i][j] == True:
					grid[i][j] = color
		return grid



grid = [
	[1, 1, 1], 
	[1, 1, 1], 
	[1, 1, 1]
]

print(grid)
print(Solution().colorBorder(grid, 1, 1, 2))


grid = [
	[1, 2, 2], 
	[2, 3, 2]
]

print(grid)
print(Solution().colorBorder(grid, 0, 1, 3))