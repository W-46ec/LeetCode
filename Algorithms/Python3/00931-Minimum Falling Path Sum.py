
"""
# Minimum Falling Path Sum

Given an `n x n` array of integers `matrix`, return *the **minimum sum** of any **falling path** through `matrix`*.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.


**Example 1:** 
![931_failing1-grid](./img/931_failing1-grid.jpg)
```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
```

**Example 2:** 
![931_failing2-grid](./img/931_failing2-grid.jpg)
```
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
```

**Constraints:** 
    - `n == matrix.length == matrix[i].length` 
    - `1 <= n <= 100` 
    - `-100 <= matrix[i][j] <= 100` 
"""

import unittest
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Dynamic programming approach
        dp[i][j] <- the minimum sum of falling path from the first row to cell matrix[i][j].
        Base case: dp[0][j] <- matrix[0][j] for all j = 0, 1, ..., n - 1.

        By definition, if we want to reach matrix[i][j], we must first reach one of the
        following cells: matrix[i - 1][j - 1], matrix[i - 1][j], or matrix[i - 1][j + 1].

        Therefore, we have the following recurrence equation:
        dp[i][j] = matrix[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]), 
        for i = 1, 2, ..., n - 1. And let dp[i - 1][k] be infinity if k is not in range [0, n).

        Eventually, we return the minimum value on the last row of dp.
        """
        n = len(matrix)
        dp = [matrix[0].copy()] + [[0] * n for _ in range(n - 1)]
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = matrix[i][j] \
                    + min(
                        dp[i - 1][j - 1] if j >= 1 else float('inf'), 
                        dp[i - 1][j], 
                        dp[i - 1][j + 1] if j < n - 1 else float('inf')
                    )
        return min(dp[-1])


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]), 13)

    def testcase2(self):
        self.assertEqual(self.soln_obj.minFallingPathSum([[-19, 57], [-40, -5]]), -59)

    def testcase3(self):
        self.assertEqual(self.soln_obj.minFallingPathSum([[97, 62], [81, -38]]), 24)

    def testcase4(self):
        self.assertEqual(self.soln_obj.minFallingPathSum([[-48]]), -48)


if __name__ == '__main__':
    unittest.main()

