
"""
# Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from typing import List
from math import inf
import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        costs = [[inf] * n for i in range(m)]
        costs[0][0] = grid[0][0]
        H = []
        for i in range(m):
            for j in range(n):
                heapq.heappush(H, [costs[i][j], i, j])
        while len(H) > 0:
            minNode = heapq.heappop(H)
            x, y = minNode[1], minNode[2]
            visited[x][y] = True
            if x > 0 and not visited[x - 1][y]:
                costs[x - 1][y] = min(costs[x - 1][y], 
                    costs[x][y] + grid[x - 1][y])
            if x < m - 1 and not visited[x + 1][y]:
                costs[x + 1][y] = min(costs[x + 1][y], 
                    costs[x][y] + grid[x + 1][y])
            if y > 0 and not visited[x][y - 1]:
                costs[x][y - 1] = min(costs[x][y - 1], 
                    costs[x][y] + grid[x][y - 1])
            if y < n - 1 and not visited[x][y + 1]:
                costs[x][y + 1] = min(costs[x][y + 1], 
                    costs[x][y] + grid[x][y + 1])
        return costs[m - 1][n - 1]

print(Solution().minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,1]
]))
