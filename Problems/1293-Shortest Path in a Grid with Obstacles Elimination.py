
"""
# Shortest Path in a Grid with Obstacles Elimination

You are given an `m x n` integer matrix `grid` where each cell is either `0` (empty) or `1` (obstacle). You can move up, down, left, or right from and to an empty cell in **one step**.

Return *the minimum number of **steps** to walk from the upper left corner `(0, 0)` to the lower right corner `(m - 1, n - 1)` given that you can eliminate **at most** `k` obstacles*. If it is not possible to find such walk return `-1`.

**Example 1:** 
```
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
```

**Example 2:** 
```
Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
```

**Constraints:** 
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 40
    1 <= k <= m * n
    grid[i][j] == 0 or 1
    grid[0][0] == grid[m - 1][n - 1] == 0

**Hint #1** 
Use BFS.

**Hint #2** 
BFS on (x,y,r) x,y is coordinate, r is remain number of obstacles you can remove.
"""


# Reference: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/solution/

from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = [(0, (0, 0, k))]        # (steps, (x, y, k))
        visited = set((0, 0, k))
        while queue:
            steps, (x, y, r) = queue.pop(0)
            
            # Reached the goal
            if x == m - 1 and y == n - 1:
                return steps
        
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    nxt_r = r - grid[x + dx][y + dy]
                    nxt_state = (x + dx, y + dy, nxt_r)
                    if nxt_r >= 0 and nxt_state not in visited:
                        visited.add(nxt_state)
                        queue.append((steps + 1, nxt_state))

        # Target not reachable
        return -1

# 6
print(Solution().shortestPath([
    [0, 0, 0], 
    [1, 1, 0], 
    [0, 0, 0], 
    [0, 1, 1], 
    [0, 0, 0]
], 1))

# -1
print(Solution().shortestPath([
    [0, 1, 1], 
    [1, 1, 1], 
    [1, 0, 0]
], 1))

