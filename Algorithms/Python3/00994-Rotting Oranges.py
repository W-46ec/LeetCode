
"""
# Rotting Oranges

You are given an `m x n` grid where each cell can have one of three values:
    - `0` representing an empty cell,
    - `1` representing a fresh orange, or
    - `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`*.


**Example 1:** 
![994_oranges](./img/994_oranges.png)
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:** 
```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:** 
```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

**Constraints:** 
    - `m == grid.length` 
    - `n == grid[i].length` 
    - `1 <= m, n <= 10` 
    - `grid[i][j]` is `0`, `1`, or `2`.
"""

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 'time' is equal to the depth of the bfs tree
        time, m, n = 0, len(grid), len(grid[0])
        # Put all rotten oranges in a queue
        queue = [(i, j, time) for i in range(m) for j in range(n) if grid[i][j] == 2]
        while queue:
            x, y, time = queue.pop(0)
            # Mark as rotten
            grid[x][y] = 2
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= x + dx < m \
                        and 0 <= y + dy < n \
                        and grid[x + dx][y + dy] == 1:
                    queue += [(x + dx, y + dy, time + 1)]
                    # Mark as explored
                    grid[x + dx][y + dy] += 10
        return -1 if sum(map(lambda row: row.count(1), grid)) > 0 else time

# 4
print(Solution().orangesRotting([
    [2, 1, 1], 
    [1, 1, 0], 
    [0, 1, 1]
]))

# -1
print(Solution().orangesRotting([
    [2, 1, 1], 
    [0, 1, 1], 
    [1, 0, 1]
]))

# 0
print(Solution().orangesRotting([
    [0, 2]
]))

# 0
print(Solution().orangesRotting([
    [0]
]))

# 1
print(Solution().orangesRotting([
    [2, 2], 
    [1, 1], 
    [0, 0], 
    [2, 0]
]))

# 0
print(Solution().orangesRotting([
    [2]
]))
