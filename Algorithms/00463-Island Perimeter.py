
"""
# Island Perimeter

You are given `row x col` `grid` representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.

Grid cells are connected **horizontally/vertically** (not diagonally). The `grid` is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


**Example 1:** 
![463_island](./img/463_island.png)
```
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
```

**Example 2:** 
```
Input: grid = [[1]]
Output: 4
```

**Example 3:** 
```
Input: grid = [[1,0]]
Output: 4
```

**Constraints:** 
    - `row == grid.length` 
    - `col == grid[i].length` 
    - `1 <= row, col <= 100` 
    - `grid[i][j]` is `0` or `1`.
    - There is exactly one island in `grid`.
```
"""

from typing import List
from itertools import product

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Optimized counting - Check only two directions
        ans, m, n = 0, len(grid), len(grid[0])

        # Traverse from left to right, top to bottom
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                # Count all 4 edges whenever we see a land cell
                ans += 4

                # If there is a land cell on the top, it means 
                # we overcounted the top edge of the current 
                # cell and the bottom edge of the cell on the top.
                # So, subtract 2 from answer
                if 0 <= i - 1 and grid[i - 1][j] == 1:
                    ans -= 2

                # Same for the land cell on the left (if any)
                if 0 <= j - 1 and grid[i][j - 1] == 1:
                    ans -= 2

                # Note that we don't have to check the right and
                # the bottom cells, since they are not yet visited.

        return ans


        # # Count naively
        # ans = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             if i > 0 and i < len(grid) - 1:
        #                 ans += 1 if grid[i - 1][j] == 0 else 0
        #                 ans += 1 if grid[i + 1][j] == 0 else 0
        #             if i == 0:
        #                 ans += 1
        #                 ans += 1 if i < len(grid) - 1 and grid[i + 1][j] == 0 else 0
        #             if i == len(grid) - 1:
        #                 ans += 1
        #                 ans += 1 if i > 0 and grid[i - 1][j] == 0 else 0
        #             if j > 0 and j < len(grid[0]) - 1:
        #                 ans += 1 if grid[i][j - 1] == 0 else 0
        #                 ans += 1 if grid[i][j + 1] == 0 else 0
        #             if j == 0:
        #                 ans += 1
        #                 ans += 1 if j < len(grid[0]) - 1 and grid[i][j + 1] == 0 else 0
        #             if j == len(grid[0]) - 1:
        #                 ans += 1
        #                 ans += 1 if j > 0 and grid[i][j - 1] == 0 else 0
        # return ans

# 16
print(Solution().islandPerimeter([
    [0, 1, 0, 0], 
    [1, 1, 1, 0], 
    [0, 1, 0, 0], 
    [1, 1, 0, 0]
]))

# 6
print(Solution().islandPerimeter([
    [0, 1, 1, 0]
]))

# 4
print(Solution().islandPerimeter([
    [1]
]))

