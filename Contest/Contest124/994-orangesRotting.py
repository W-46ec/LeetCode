class Solution:
	def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
		miniute = 0
		if sum([i.count(2) for i in grid]) == 0:
			if sum([i.count(1) for i in grid]):
				return -1
			else:
				return 0

		def hasRotten(grid, x, y):
			if x > 0 and grid[x - 1][y] == 2:
				return True
			if x < len(grid) - 1 and grid[x + 1][y] == 2:
				return True
			if y > 0 and grid[x][y - 1] == 2:
				return True
			if y < len(grid[0]) - 1 and grid[x][y + 1] == 2:
				return True
			return False

		def isIsolated(grid, x, y):
			if x > 0 and grid[x - 1][y] != 0:
				return False
			if x < len(grid) - 1 and grid[x + 1][y] != 0:
				return False
			if y > 0 and grid[x][y - 1] != 0:
				return False
			if y < len(grid[0]) - 1 and grid[x][y + 1] != 0:
				return False
			return True

		while sum([i.count(1) for i in grid]):
			queue = []
			for i in range(len(grid)):
				for j in range(len(grid[0])):
					if grid[i][j] == 1:
						if hasRotten(grid, i, j):
							queue.append((i, j))
						if isIsolated(grid, i, j):
							return -1
			if len(queue) == 0:
				break
			for pos in queue:
				grid[pos[0]][pos[1]] = 2
			miniute += 1
		if sum([i.count(1) for i in grid]):
			return -1
		else:
			return miniute


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(Solution().orangesRotting([[0, 2]]))
print(Solution().orangesRotting([[0]]))
print(Solution().orangesRotting([[2],[2],[1],[0],[1],[1]]))