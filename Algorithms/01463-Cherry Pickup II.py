
"""
# Cherry Pickup II

You are given a `rows x cols` matrix `grid` representing a field of cherries where `grid[i][j]` represents the number of cherries that you can collect from the `(i, j)` cell.

You have two robots that can collect cherries for you:
    - **Robot #1** is located at the **top-left corner** `(0, 0)`, and
    - **Robot #2** is located at the **top-right corner** `(0, cols - 1)`.

Return *the maximum number of cherries collection using both robots by following the rules below*:
    - From a cell `(i, j)`, robots can move to cell `(i + 1, j - 1)`, `(i + 1, j)`, or `(i + 1, j + 1)`.
    - When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
    - When both robots stay in the same cell, only one takes the cherries.
    - Both robots cannot move outside of the grid at any moment.
    - Both robots should reach the bottom row in `grid`.

**Example 1:** 
![1463_sample_1_1802](./img/1463_sample_1_1802.png)
```
Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
```

**Example 2:** 
![1463_sample_2_1802](./img/1463_sample_2_1802.png)
```
Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
```

**Constraints:** 
    - `rows == grid.length` 
    - `cols == grid[i].length` 
    - `2 <= rows, cols <= 70` 
    - `0 <= grid[i][j] <= 100` 

**Hint 1** 
Use dynammic programming, define DP[i][j][k]: The maximum cherries that both robots can take starting on the ith row, and column j and k of Robot 1 and 2 respectively.
"""

from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[r][c1][c2] -- Optimal solution if we start from the rth row
        #                  with the two robots at positions c1 and c2.
        # r, c1, c2 are 1-indexed:
        #     r <- 1, 2, ..., m
        #     c1, c2 <- 1, 2, ..., n
        dp = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c1 in range(1, n + 1):
                for c2 in range(1, n + 1):
                    dp[r][c1][c2] += grid[r][c1 - 1]
                    dp[r][c1][c2] += grid[r][c2 - 1] if c1 != c2 else 0
                    dp[r][c1][c2] += max([
                        dp[r + 1][prev_c1][prev_c2]
                            for prev_c1 in range(c1 - 1, c1 + 2)
                            for prev_c2 in range(c2 - 1, c2 + 2)
                    ])
        return dp[0][1][n]

# 24
print(Solution().cherryPickup([
    [3, 1, 1], 
    [2, 5, 1], 
    [1, 5, 5], 
    [2, 1, 1]
]))

# 28
print(Solution().cherryPickup([
    [1, 0, 0, 0, 0, 0, 1], 
    [2, 0, 0, 0, 0, 3, 0], 
    [2, 0, 9, 0, 0, 0, 0], 
    [0, 3, 0, 5, 4, 0, 0], 
    [1, 0, 2, 3, 0, 0, 6]
]))
