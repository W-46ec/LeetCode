
from typing import List

class Solution:
	def closedIsland(self, grid: List[List[int]]) -> int:
		ans = 0
		r, c = len(grid), len(grid[0])
		visited = [[False] * c for i in range(r)]
		def bfs(x, y, search, mark):
			queue = [(x, y)]
			while len(queue):
				x, y = queue.pop(0)
				if not visited[x][y]:
					visited[x][y] = True
					grid[x][y] = mark
					if x > 0 and not visited[x - 1][y] and grid[x - 1][y] == search:
						queue.append((x - 1, y))
					if x < r - 1 and not visited[x + 1][y] and grid[x + 1][y] == search:
						queue.append((x + 1, y))
					if y > 0 and not visited[x][y - 1] and grid[x][y - 1] == search:
						queue.append((x, y - 1))
					if y < c - 1 and not visited[x][y + 1] and grid[x][y + 1] == search:
						queue.append((x, y + 1))
		for i in range(r):
			if grid[i][0] == 0:
				bfs(i, 0, 0, -1)
			if grid[i][c - 1] == 0:
				bfs(i, c - 1, 0, -1)
		for j in range(c):
			if grid[0][j] == 0:
				bfs(0, j, 0, -1)
			if grid[r - 1][j] == 0:
				bfs(r - 1, j, 0, -1)
		for i in range(r):
			for j in range(c):
				if grid[i][j] == 0:
					bfs(i, j, 0, -1)
					ans += 1
		return ans

grid = [
	[1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1]
]

print(Solution().closedIsland(grid))

