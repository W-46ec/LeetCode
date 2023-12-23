
"""
# Path Crossing

Given a string `path`, where `path[i] = 'N'`, `'S'`, `'E'` or `'W'`, each representing moving one unit north, south, east, or west, respectively. You start at the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`.

Return *`true` if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited*. Return `false` otherwise.


**Example 1:** 
![1496_screen-shot-2020-06-10-at-123929-pm](./img/1496_screen-shot-2020-06-10-at-123929-pm.png)
```
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
```

**Example 2:** 
![1496_screen-shot-2020-06-10-at-123843-pm](./img/1496_screen-shot-2020-06-10-at-123843-pm.png)
```
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
```

**Constraints:** 
    - `1 <= path.length <= 10^4` 
    - `path[i]` is either `'N'`, `'S'`, `'E'`, or `'W'`.
"""

import unittest

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {
            'N': (0, 1), 
            'S': (0, -1), 
            'E': (1, 0), 
            'W': (-1, 0)
        }

        currX, currY, visited = 0, 0, {(0, 0)}
        for d in path:
            dx, dy = directions[d]
            currX, currY = currX + dx, currY + dy
            if (currX, currY) in visited:
                return True
            visited.add((currX, currY))
        return False


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.isPathCrossing("NES"), False)

    def testcase2(self):
        self.assertEqual(self.soln_obj.isPathCrossing("NESWW"), True)

    def testcase3(self):
        self.assertEqual(self.soln_obj.isPathCrossing("NNSWWEWSSESSWENNW"), True)


if __name__ == '__main__':
    unittest.main()
