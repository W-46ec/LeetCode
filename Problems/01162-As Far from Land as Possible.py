
"""
# As Far from Land as Possible

Given an `n x n` grid containing only values `0` and `1`, where `0` represents water and `1` represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return `-1`.

The distance used in this problem is the Manhattan distance: the distance between two cells `(x0, y0)` and `(x1, y1)` is `|x0 - x1| + |y0 - y1|`.


**Example 1:** 
![1162_1336_ex1](./img/1162_1336_ex1.jfif)
```
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
```

**Example 2:** 
![1162_1336_ex2](./img/1162_1336_ex2.jfif)
```
Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
```

**Constraints:** 
    - `n == grid.length` 
    - `n == grid[i].length` 
    - `1 <= n <= 100` 
    - `grid[i][j]` is `0` or `1` 
"""

from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # Start from the lands and explore the map using BFS
        # Set initial distance to 0 and record the cumulated distance after each iteration

        n = len(grid)
        visited, queue = [[False] * n for _ in range(n)], []

        # Enqueue all lands & set distance to 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    queue += [(x, y, 0)]
                    visited[x][y] = True

        # BFS
        max_dist = -1
        while 0 < len(queue) < n ** 2:
            x, y, dist = queue.pop(0)
            max_dist = max(max_dist, dist)
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < n \
                        and 0 <= y + dy < n \
                        and not visited[x + dx][y + dy]:
                    queue += [(x + dx, y + dy, dist + 1)]
                    visited[x + dx][y + dy] = True
        return max_dist

# 2
print(Solution().maxDistance([
    [1, 0, 1], 
    [0, 0, 0], 
    [1, 0, 1]
]))

# 4
print(Solution().maxDistance([
    [1, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]))
