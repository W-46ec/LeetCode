
"""
# Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A *clear path from top-left to bottom-right* has length `k` if and only if it is composed of cells `C_1, C_2, ..., C_k` such that:
    - Adjacent cells `C_i` and `C_{i+1}` are connected 8-directionally (ie., they are different and share an edge or corner)
    - `C_1` is at location `(0, 0)` (ie. has value `grid[0][0]`)
    - `C_k` is at location `(N-1, N-1)` (ie. has value `grid[N-1][N-1]`)
    - If `C_i` is located at `(r, c)`, then `grid[r][c]` is empty (ie. `grid[r][c] == 0`).

Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.


**Example 1:** 
```
Input: [[0,1],[1,0]]
![1091_example1_1](./img/1091_example1_1.png)

Output: 2
![1091_example1_2](./img/1091_example1_2.png)
```

**Example 2:** 
```
Input: [[0,0,0],[1,1,0],[1,1,0]]
![1091_example2_1](./img/1091_example2_1.png)

Output: 4
![1091_example2_2](./img/1091_example2_2.png)
```

**Note:** 
    - `1 <= grid.length == grid[0].length <= 100` 
    - `grid[r][c]` is `0` or `1` 

**Hint #1** 
Do a breadth first search to find the shortest path.
"""

from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = [(0, 0, 1)]     # x, y, cost
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        visited[0][0] = True
        while queue:
            x, y, cost = queue[0]
            queue[0 : 1] = []
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return cost
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < len(grid) \
                            and 0 <= y + dy < len(grid[0]) \
                            and not visited[x + dx][y + dy] \
                            and grid[x + dx][y + dy] == 0:
                        visited[x + dx][y + dy] = True
                        queue[len(queue) : len(queue)] = [(x + dx, y + dy, cost + 1)]
        return -1

# 2
print(Solution().shortestPathBinaryMatrix([
    [0, 1], 
    [1, 0]
]))

# 4
print(Solution().shortestPathBinaryMatrix([
    [0, 0, 0], 
    [1, 1, 0], 
    [1, 1, 0]
]))

# -1
print(Solution().shortestPathBinaryMatrix([
    [0, 0, 0], 
    [1, 1, 0], 
    [1, 1, 1]
]))

# 146
print(Solution().shortestPathBinaryMatrix([[0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1],[1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,0,1,1],[0,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,1],[0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0],[0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0],[1,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1],[0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0],[1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1],[1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0],[0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1],[1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1],[0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0],[1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1],[0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0],[0,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0],[0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0],[0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0],[1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1],[0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,1,0,0,0,0],[1,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0],[0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0],[1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1],[1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1],[1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1],[0,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1],[0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1],[1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1],[1,0,0,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,0],[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0],[1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1],[1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0],[0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1],[0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,0],[0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0],[1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1],[1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0],[0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,1],[0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],[1,1,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1],[0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,1],[1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1],[1,1,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1],[0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,0],[1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0],[0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0],[1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0],[0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0],[1,1,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0],[1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1],[0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0],[1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1],[1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,1,1],[1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1],[1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,1],[0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1],[1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0],[0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1],[0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,0,1],[0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0],[0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1],[0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,0,0],[0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1],[0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0],[0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1],[1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0],[0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0],[1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,0,0,1,1,0,1],[1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0],[1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1],[0,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0],[0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0],[1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,0],[1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,1,1,1],[0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0],[0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0],[0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0],[0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1],[1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1],[0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1],[1,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0],[1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0],[0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1],[0,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1],[1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0],[1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0],[1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1],[0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1],[1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1],[0,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1],[1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0],[0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1],[0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1],[0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0],[0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1],[0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0],[0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0]]))

