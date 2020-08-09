
"""
# Rotting Oranges

In a given grid, each cell can have one of three values:

the value `0` representing an empty cell;
the value `1` representing a fresh orange;
the value `2` representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return `-1` instead.


**Example 1:** 
![994_oranges](./img/994_oranges.png)
```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:** 
```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:** 
```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```

**Note:** 
    - `1 <= grid.length <= 10` 
    - `1 <= grid[0].length <= 10` 
    - `grid[i][j]` is only `0`, `1`, or `2`.
"""

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, queue = 0, [(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2]
        while queue:
            x, y, level = queue.pop(0)
            time, grid[x][y] = level if level > time else time, 2
            for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if x + i in range(len(grid)) and y + j in range(len(grid[0])) and grid[x + i][y + j] == 1:
                    queue += [(x + i, y + j, level + 1)]
                    grid[x + i][y + j] += 10
        return -1 if any(map(lambda lst: 1 in lst, grid)) else time

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
