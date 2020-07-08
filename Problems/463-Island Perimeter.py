
"""
# Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


**Example:** 
```
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

![463_island](./img/463_island.png)
```
"""

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i > 0 and i < len(grid) - 1:
                        ans += 1 if grid[i - 1][j] == 0 else 0
                        ans += 1 if grid[i + 1][j] == 0 else 0
                    if i == 0:
                        ans += 1
                        ans += 1 if i < len(grid) - 1 and grid[i + 1][j] == 0 else 0
                    if i == len(grid) - 1:
                        ans += 1
                        ans += 1 if i > 0 and grid[i - 1][j] == 0 else 0
                    if j > 0 and j < len(grid[0]) - 1:
                        ans += 1 if grid[i][j - 1] == 0 else 0
                        ans += 1 if grid[i][j + 1] == 0 else 0
                    if j == 0:
                        ans += 1
                        ans += 1 if j < len(grid[0]) - 1 and grid[i][j + 1] == 0 else 0
                    if j == len(grid[0]) - 1:
                        ans += 1
                        ans += 1 if j > 0 and grid[i][j - 1] == 0 else 0
        return ans

print(Solution().islandPerimeter([
    [0, 1, 0, 0], 
    [1, 1, 1, 0], 
    [0, 1, 0, 0], 
    [1, 1, 0, 0]
]))     # 16

print(Solution().islandPerimeter([
    [0, 1, 1, 0]
]))     # 6

print(Solution().islandPerimeter([
    [1]
]))     # 4
