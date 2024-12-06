
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
![1861_rotatingtheboxleetcodewithstones](./img/1861_rotatingtheboxleetcodewithstones.png)
```
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
```

**Example 2:** 
![1861_rotatingtheboxleetcode2withstones](./img/1861_rotatingtheboxleetcode2withstones.png)
```
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
```

**Example 3:** 
![1861_rotatingtheboxleetcode3withstone](./img/1861_rotatingtheboxleetcode3withstone.png)
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
        box_rotated = [['.'] * m for _ in range(n)]
        for i in range(m):
            j = n - 1
            while j >= 0:
                if box[i][j] == '#':
                    target_j = j
                    while target_j + 1 < n and box[i][target_j + 1] == '.':
                        target_j += 1
                    box[i][j], box[i][target_j] = box[i][target_j], box[i][j]
                    box_rotated[target_j][m - i - 1] = box[i][target_j]
                box_rotated[j][m - i - 1] = box[i][j]
                j -= 1
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
