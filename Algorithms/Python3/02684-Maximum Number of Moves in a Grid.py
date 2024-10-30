
"""
# Maximum Number of Moves in a Grid

You are given a **0-indexed** `m x n` matrix `grid` consisting of **positive** integers.

You can start at **any** cell in the first column of the matrix, and traverse the grid in the following way:
- From a cell `(row, col)`, you can move to any of the cells: `(row - 1, col + 1)`, `(row, col + 1)` and `(row + 1, col + 1)` such that the value of the cell you move to, should be **strictly** bigger than the value of the current cell.

Return *the **maximum** number of **moves** that you can perform*.


**Example 1:**
![2684_yetgriddrawio-10](./img/2684_yetgriddrawio-10.png)
```
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
```

**Example 2:** 
![2684_yetgrid4drawio](./img/2684_yetgrid4drawio.png)
```
Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
```

**Constraints:** 
    - `m == grid.length` 
    - `n == grid[i].length` 
    - `2 <= m, n <= 1000` 
    - `4 <= m * n <= 10^5` 
    - `1 <= grid[i][j] <= 10^6` 
"""

import unittest
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # DP - Buttom-up solution
        # dp[i][j] <- max moves you can perform if starting from grid[i][j]
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for j in range(n - 1, 0, -1):
            for i in range(m):
                if i >= 1 and grid[i - 1][j] > grid[i][j - 1]:
                    dp[i][j - 1] = max(dp[i][j - 1], 1 + dp[i - 1][j])
                if grid[i][j] > grid[i][j - 1]:
                    dp[i][j - 1] = max(dp[i][j - 1], 1 + dp[i][j])
                if i < m - 1 and grid[i + 1][j] > grid[i][j - 1]:
                    dp[i][j - 1] = max(dp[i][j - 1], 1 + dp[i + 1][j])
        return max([dp[i][0] for i in range(m)])


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.maxMoves([
            [2, 4, 3, 5], 
            [5, 4, 9, 3], 
            [3, 4, 2, 11], 
            [10, 9, 13, 15]
        ]), 3)

    def testcase2(self):
        self.assertEqual(self.soln_obj.maxMoves([
            [3, 2, 4], 
            [2, 1, 9], 
            [1, 1, 7]
        ]), 0)

    def testcase3(self):
        self.assertEqual(self.soln_obj.maxMoves([
            [65, 200, 263, 220, 91, 183, 2, 187, 175, 61, 225, 120, 39], 
            [111, 242, 294, 31, 241, 90, 145, 25, 262, 214, 145, 71, 294], 
            [152, 25, 240, 69, 279, 238, 222, 9, 137, 277, 8, 143, 143], 
            [189, 31, 86, 250, 20, 63, 188, 209, 75, 22, 127, 272, 110], 
            [122, 94, 298, 25, 90, 169, 68, 3, 208, 274, 202, 135, 275], 
            [205, 20, 171, 90, 70, 272, 280, 138, 142, 151, 80, 122, 130], 
            [284, 272, 271, 269, 265, 134, 185, 243, 247, 50, 283, 20, 232], 
            [266, 236, 265, 234, 249, 62, 98, 130, 122, 226, 285, 168, 204], 
            [231, 24, 256, 101, 142, 28, 268, 82, 111, 63, 115, 13, 144], 
            [277, 277, 31, 144, 49, 132, 28, 138, 133, 29, 286, 45, 93], 
            [163, 96, 25, 9, 3, 159, 148, 59, 25, 81, 233, 127, 12], 
            [127, 38, 31, 209, 300, 256, 15, 43, 74, 64, 73, 141, 200]
        ]), 3)


if __name__ == '__main__':
    unittest.main()
