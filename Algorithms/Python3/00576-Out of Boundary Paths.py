
"""
# Out of Boundary Paths

There is an `m x n` grid with a ball. The ball is initially at the position `[startRow, startColumn]`. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply **at most** `maxMove` moves to the ball.

Given the five integers `m`, `n`, `maxMove`, `startRow`, `startColumn`, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it **modulo** `10^9 + 7`.


**Example 1:** 
![576_out_of_boundary_paths_1](./img/576_out_of_boundary_paths_1.png)
```
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
```

**Example 2:** 
![576_out_of_boundary_paths_2](./img/576_out_of_boundary_paths_2.png)
```
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
```

**Constraints:** 
    - `1 <= m, n <= 50` 
    - `0 <= maxMove <= 50` 
    - `0 <= startRow < m` 
    - `0 <= startColumn < n` 
"""

import unittest
from itertools import product

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        num_paths = [[0] * n for _ in range(m)]
        num_paths[startRow][startColumn] = 1
        count, MOD = 0, 10 ** 9 + 7
        for _ in range(maxMove):
            num_paths_nxt = [[0] * n for _ in range(m)]
            for x, y in product(range(m), range(n)):
                count += sum([b * num_paths[x][y] for b in [x == 0, x == m - 1, y == 0, y == n - 1]]) % MOD
                moves = 0
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        moves += num_paths[x + dx][y + dy]
                num_paths_nxt[x][y] = moves % MOD
            num_paths = num_paths_nxt
        return count % MOD


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findPaths(2, 2, 2, 0, 0), 6)

    def testcase2(self):
        self.assertEqual(self.soln_obj.findPaths(1, 3, 3, 0, 1), 12)


if __name__ == '__main__':
    unittest.main()
