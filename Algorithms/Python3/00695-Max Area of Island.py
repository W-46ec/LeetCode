
"""
# Max Area of Island

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return *the maximum **area** of an island in `grid`*. If there is no island, return `0`.


**Example 1:** 
![695_maxarea1-grid](./img/695_maxarea1-grid.jpg)
```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:** 
```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

**Constraints:** 
    - `m == grid.length` 
    - `n == grid[i].length` 
    - `1 <= m, n <= 50` 
    - `grid[i][j]` is either `0` or `1`.
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited, ans = [[False] * len(grid[0]) for _ in range(len(grid))], 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] and not visited[x][y]:
                    queue, visited[x][y] = [(x, y)], True
                    for i, j in queue:
                        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if 0 <= i + di < len(grid) \
                                    and 0 <= j + dj < len(grid[0]) \
                                    and grid[i + di][j + dj] \
                                    and not visited[i + di][j + dj]:
                                visited[i + di][j + dj] = True
                                queue[len(queue) :] = [(i + di, j + dj)]
                    ans = max(ans, len(queue))
        return ans

# 6
print(Solution().maxAreaOfIsland([
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], 
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]))

# 0
print(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))

# 4
print(Solution().maxAreaOfIsland([
    [1, 1, 0, 0, 0], 
    [1, 1, 0, 0, 0], 
    [0, 0, 0, 1, 1], 
    [0, 0, 0, 1, 1]
]))
