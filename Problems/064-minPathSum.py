
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
from heapq import heappush, heappop

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        costs = [[float('inf')] * n for i in range(m)]
        costs[0][0] = grid[0][0]
        Heap = [(costs[0][0], 0, 0)]
        while Heap:
            min_cost, x, y = heappop(Heap)
            if (x, y) == (m - 1, n - 1):
                return min_cost
            for dx, dy in [[1, 0], [0, 1]]:
                if x + dx in range(m) and y + dy in range(n):
                    new_cost = min_cost + grid[x + dx][y + dy]
                    if new_cost < costs[x + dx][y + dy]:
                        costs[x + dx][y + dy] = new_cost
                        heappush(Heap, (new_cost, x + dx, y + dy))

# 7
print(Solution().minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))

# 82
print(Solution().minPathSum([
    [5, 4, 2, 9, 6, 0, 3, 5, 1, 4, 9, 8, 4, 9, 7, 5, 1], 
    [3, 4, 9, 2, 9, 9, 0, 9, 7, 9, 4, 7, 8, 4, 4, 5, 8], 
    [6, 1, 8, 9, 8, 0, 3, 7, 0, 9, 8, 7, 4, 9, 2, 0, 1], 
    [4, 0, 0, 5, 1, 7, 4, 7, 6, 4, 1, 0, 1, 0, 6, 2, 8], 
    [7, 2, 0, 2, 9, 3, 4, 7, 0, 8, 9, 5, 9, 0, 1, 1, 0], 
    [8, 2, 9, 4, 9, 7, 9, 3, 7, 0, 3, 6, 5, 3, 5, 9, 6], 
    [8, 9, 9, 2, 6, 1, 2, 5, 8, 3, 7, 0, 4, 9, 8, 8, 8], 
    [5, 8, 5, 4, 1, 5, 6, 6, 3, 3, 1, 8, 3, 9, 6, 4, 8], 
    [0, 2, 2, 3, 0, 2, 6, 7, 2, 3, 7, 3, 1, 5, 8, 1, 3], 
    [4, 4, 0, 2, 0, 3, 8, 4, 1, 3, 3, 0, 7, 4, 2, 9, 8], 
    [5, 9, 0, 4, 7, 5, 7, 6, 0, 8, 3, 0, 0, 6, 6, 6, 8], 
    [0, 7, 1, 8, 3, 5, 1, 8, 7, 0, 2, 9, 2, 2, 7, 1, 5], 
    [1, 0, 0, 0, 6, 2, 0, 0, 2, 2, 8, 0, 9, 7, 0, 8, 0], 
    [1, 1, 7, 2, 9, 6, 5, 4, 8, 7, 8, 5, 0, 3, 8, 1, 5], 
    [8, 9, 7, 8, 1, 1, 3, 0, 1, 2, 9, 4, 0, 1, 5, 3, 1], 
    [9, 2, 7, 4, 8, 7, 3, 9, 2, 4, 2, 2, 7, 8, 2, 6, 7], 
    [3, 8, 1, 6, 0, 4, 8, 9, 8, 0, 2, 5, 3, 5, 5, 7, 5], 
    [1, 8, 2, 5, 7, 7, 1, 9, 9, 8, 9, 2, 4, 9, 5, 4, 0], 
    [3, 4, 4, 1, 5, 3, 3, 8, 8, 6, 3, 5, 3, 8, 7, 1, 3]
]))