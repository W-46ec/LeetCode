
from typing import List

class Solution:
	def countServers(self, grid: List[List[int]]) -> int:
		m, n, ans = len(grid), len(grid[0]), 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					hasOne = False
					if grid[i].count(1) >= 2:
						hasOne = True
					if [grid[k][j] for k in range(m)].count(1) >= 2:
						hasOne = True
					ans += 1 if hasOne else 0
		return ans

print(Solution().countServers([
	[1, 0], 
	[0, 1]
]))

print(Solution().countServers([
	[1, 0], 
	[1, 1]
]))

print(Solution().countServers([
	[1, 1, 0, 0], 
	[0, 0, 1, 0], 
	[0, 0, 1, 0], 
	[0, 0, 0, 1]
]))
