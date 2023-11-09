
"""
# Determine if a Cell Is Reachable at a Given Time

You are given four integers `sx`, `sy`, `fx`, `fy`, and a **non-negative** integer `t`.

In an infinite 2D grid, you start at the cell `(sx, sy)`. Each second, you **must** move to any of its adjacent cells.

Return *`true` if you can reach cell `(fx, fy)` after **exactly** `t` **seconds**, or `false` otherwise*.

A cell's **adjacent cells** are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.


**Example 1:** 
![2849_example2](./img/2849_example2.svg)
```
Input: sx = 2, sy = 4, fx = 7, fy = 7, t = 6
Output: true
Explanation: Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted in the picture above. 
```

**Example 2:** 
![2849_example1](./img/2849_example1.svg)
```
Input: sx = 3, sy = 1, fx = 7, fy = 3, t = 3
Output: false
Explanation: Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.
```

**Constraints:** 
    - `1 <= sx, sy, fx, fy <= 10^9` 
    - `0 <= t <= 10^9` 
"""

import unittest

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx, dy = abs(fx - sx), abs(fy - sy)
        dist = abs(dx - dy) + min(dx, dy)
        return t >= dist if dist > 0 else t == 0 or t >= 2


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.isReachableAtTime(2, 4, 7, 7, 6), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.isReachableAtTime(3, 1, 7, 3, 3), False)

    def testcase3(self):
        self.assertEqual(self.soln_obj.isReachableAtTime(1, 2, 1, 2, 0), True)

    def testcase4(self):
        self.assertEqual(self.soln_obj.isReachableAtTime(1, 2, 1, 2, 1), False)

    def testcase5(self):
        self.assertEqual(self.soln_obj.isReachableAtTime(1, 2, 1, 2, 2), True)

    def testcase6(self):
        self.assertEqual(self.soln_obj.isReachableAtTime(1, 2, 1, 2, 3), True)


if __name__ == '__main__':
    unittest.main()

