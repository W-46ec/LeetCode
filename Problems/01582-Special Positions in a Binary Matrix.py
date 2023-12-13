
"""
# Special Positions in a Binary Matrix

Given an `m x n` binary matrix `mat`, return *the number of special positions in `mat`*.

A position `(i, j)` is called **special** if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0` (rows and columns are **0-indexed**).


**Example 1:** 
![1582_special1](./img/1582_special1.jpg)
```
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
```

**Example 2:** 
![1582_special-grid](./img/1582_special-grid.jpg)
```
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
```

**Constraints:** 
    - `m == mat.length` 
    - `n == mat[i].length` 
    - `1 <= m, n <= 100` 
    - `mat[i][j]` is either `0` or `1`.
"""

import unittest
from typing import List
from itertools import product

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Compute the sum of each row and each column respectively
        sum_row = [sum(x) for x in mat]
        sum_col = [sum(x) for x in zip(*mat)]
        # Position (i, j) is special if mat[i][j] is 1 and the
        # sum of the corresponding row and column are both 1.
        m, n, count = len(mat), len(mat[0]), 0
        for i, j in product(range(m), range(n)):
            if mat[i][j] and sum_row[i] == 1 and sum_col[j] == 1:
                count += 1
        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]), 1)

    def testcase2(self):
        self.assertEqual(self.soln_obj.numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)

    def testcase3(self):
        self.assertEqual(self.soln_obj.numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]]), 2)


if __name__ == '__main__':
    unittest.main()

