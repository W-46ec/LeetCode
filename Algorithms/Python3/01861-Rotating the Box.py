
"""
# Rotating the Box

You are given an `m x n` matrix of characters `box` representing a side-view of a box. Each cell of the box is one of the following:
    - A stone `'#'` 
    - A stationary obstacle `'*'` 
    - Empty `'.'` 

The box is rotated **90 degrees clockwise**, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity **does not** affect the obstacles' positions, and the inertia from the box's rotation **does not** affect the stones' horizontal positions.

It is **guaranteed** that each stone in `box` rests on an obstacle, another stone, or the bottom of the box.

Return *an `n x m` matrix representing the box after the rotation described above*.


**Example 1:** 

```
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
```

**Example 2:** 

```
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
```

**Example 3:** 

```
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
```

**Constraints:** 
    - `m == box.length` 
    - `n == box[i].length` 
    - `1 <= m, n <= 500` 
    - `box[i][j]` is either `'#'`, `'*'`, or `'.'`.
"""

import unittest
from typing import List
from itertools import product

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        box_rotated = [[None] * m for _ in range(n)]

        # Rotation
        for i, j in product(range(m), range(n)):
            box_rotated[j][m - i - 1] = box[i][j]

        # Falling
        for j in range(m):
            i = n - 1
            while i >= 0:
                if i >= 0 and box_rotated[i][j] == '#':
                    target_i = i
                    while target_i + 1 < n and box_rotated[target_i + 1][j] == '.':
                        target_i += 1
                    box_rotated[i][j], box_rotated[target_i][j] = box_rotated[target_i][j], box_rotated[i][j]
                i -= 1

        return box_rotated


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        box = [['#', '.', '#']]
        expected = [['.'], ['#'], ['#']]
        ans = self.soln_obj.rotateTheBox(box)
        self.assertEqual(len(ans), len(box[0]))
        self.assertEqual(len(ans[0]), len(box))
        self.assertEqual(all([expected[i] == ans[i] for i in range(len(expected))]), True)

    def testcase2(self):
        box = [['#', '.', '*', '.'], ['#', '#', '*', '.']]
        expected = [['#', '.'], ['#', '#'], ['*', '*'], ['.', '.']]
        ans = self.soln_obj.rotateTheBox(box)
        self.assertEqual(len(ans), len(box[0]))
        self.assertEqual(len(ans[0]), len(box))
        self.assertEqual(all([expected[i] == ans[i] for i in range(len(expected))]), True)

    def testcase3(self):
        box = [['#', '#', '*', '.', '*', '.'], ['#', '#', '#', '*', '.', '.'], ['#', '#', '#', '.', '#', '.']]
        expected = [['.', '#', '#'], ['.', '#', '#'], ['#', '#', '*'], ['#', '*', '.'], ['#', '.', '*'], ['#', '.', '.']]
        ans = self.soln_obj.rotateTheBox(box)
        self.assertEqual(len(ans), len(box[0]))
        self.assertEqual(len(ans[0]), len(box))
        self.assertEqual(all([expected[i] == ans[i] for i in range(len(expected))]), True)

    def testcase4(self):
        box = [['#', '#', '*', '.', '*', '.'], ['#', '#', '#', '*', '#', '.'], ['#', '#', '#', '.', '#', '.']]
        expected = [['.', '#', '#'], ['.', '#', '#'], ['#', '#', '*'], ['#', '*', '.'], ['#', '.', '*'], ['#', '#', '.']]
        ans = self.soln_obj.rotateTheBox(box)
        self.assertEqual(len(ans), len(box[0]))
        self.assertEqual(len(ans[0]), len(box))
        self.assertEqual(all([expected[i] == ans[i] for i in range(len(expected))]), True)


if __name__ == '__main__':
    unittest.main()
