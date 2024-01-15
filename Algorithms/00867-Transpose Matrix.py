
"""
# Transpose Matrix

Given a 2D integer array `matrix`, return *the **transpose** of `matrix`.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
![867_hint_transpose](./img/867_hint_transpose.png)


**Example 1:** 
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

**Example 2:** 
```
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

**Constraints:** 
    - `m == matrix.length` 
    - `n == matrix[i].length` 
    - `1 <= m, n <= 1000` 
    - `1 <= m * n <= 10^5` 
    - `-10^9 <= matrix[i][j] <= 10^9` 
"""

import unittest
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [x for x in zip(*matrix)]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ans = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        m, n = len(ans), len(ans[0])
        transposed = self.soln_obj.transpose(matrix)
        self.assertEqual(len(transposed), m)
        self.assertEqual(len(transposed[0]), n)
        for i in range(m):
            for j in range(n):
                self.assertEqual(transposed[i][j], ans[i][j])

    def testcase2(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        ans = [[1, 4], [2, 5], [3, 6]]
        m, n = len(ans), len(ans[0])
        transposed = self.soln_obj.transpose(matrix)
        self.assertEqual(len(transposed), m)
        self.assertEqual(len(transposed[0]), n)
        for i in range(m):
            for j in range(n):
                self.assertEqual(transposed[i][j], ans[i][j])


if __name__ == '__main__':
    unittest.main()
