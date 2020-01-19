class Solution:
	def surfaceArea(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		n = len(grid)
		surface = 2 * sum([n - i.count(0) for i in grid])
		while sum([sum(i) for i in grid]) != 0:
			for i in range(n):
				for j in range(n):
					if grid[i][j] != 0:
						if i == 0 or grid[i - 1][j] == 0:
							surface += 1
						if i == n - 1 or grid[i + 1][j] == 0:
							surface += 1
						if j == 0 or grid[i][j - 1] == 0:
							surface += 1
						if j == n - 1 or grid[i][j + 1] == 0:
							surface += 1
			for i in range(n):
				for j in range(n):
					if grid[i][j] > 0:
						grid[i][j] -= 1
		return surface

print(Solution().surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))