
"""
# Unique Paths III

You are given an `m x n` integer array `grid` where `grid[i][j]` could be:
    - `1` representing the starting square. There is exactly one starting square.
    - `2` representing the ending square. There is exactly one ending square.
    - `0` representing empty squares we can walk over.
    - `-1` representing obstacles that we cannot walk over.

Return *the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once*.


**Example 1:** 
![980_lc-unique1](./img/980_lc-unique1.jpg)
```
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
```

**Example 2:** 
![980_lc-unique2](./img/980_lc-unique2.jpg)
```
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
```

**Example 3:** 
![980_lc-unique3](./img/980_lc-unique3.jpg)
```
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
```

**Constraints:** 
    - `m == grid.length` 
    - `n == grid[i].length` 
    - `1 <= m, n <= 20` 
    - `1 <= m * n <= 20` 
    - `-1 <= grid[i][j] <= 2` 
    - There is exactly one starting cell and one ending cell.
"""

from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Find out the starting and ending location
        # and how long the target path should be
        target_len = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                elif grid[i][j] == 2:
                    end_i, end_j = i, j
                if grid[i][j] != -1:
                    target_len += 1

        path_count = 0
        visited = [[False] * n for _ in range(m)]
        def backtracking_dfs(x = start_i, y = start_j, curr_len = 1):
            nonlocal path_count
            visited[x][y] = True
            if x == end_i and y == end_j:
                path_count += 1 if curr_len == target_len else 0
                return
            for dx, dy in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                if 0 <= x + dx < m and 0 <= y + dy < n \
                        and grid[x + dx][y + dy] != -1 \
                        and not visited[x + dx][y + dy]:
                    backtracking_dfs(x + dx, y + dy, curr_len + 1)
                    visited[x + dx][y + dy] = False

        backtracking_dfs()
        return path_count

# 2
print(Solution().uniquePathsIII([
    [1, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 2, -1]
]))

# 4
print(Solution().uniquePathsIII([
    [1, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 2]
]))

# 0
print(Solution().uniquePathsIII([
    [0, 1], 
    [2, 0]
]))
