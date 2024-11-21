
"""
# Count Unguarded Cells in the Grid

You are given two integers `m` and `n` representing a **0-indexed** `m x n` grid. You are also given two 2D integer arrays `guards` and `walls` where `guards[i] = [row_i, col_i]` and `walls[j] = [row_j, col_j]` represent the positions of the `ith` guard and `jth` wall respectively.

A guard can see **every** cell in the four cardinal directions (north, east, south, or west) starting from their position unless **obstructed** by a wall or another guard. A cell is **guarded** if there is **at least** one guard that can see it.

Return *the number of unoccupied cells that are **not guarded***.


**Example 1:** 
![2257_example1drawio2](./img/2257_example1drawio2.png)
```
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
```

**Example 2:** 
![2257_example2drawio](./img/2257_example2drawio.png)
```
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
```

**Constraints:** 
    - `1 <= m, n <= 10^5` 
    - `2 <= m * n <= 10^5` 
    - `1 <= guards.length, walls.length <= 5 * 10^4` 
    - `2 <= guards.length + walls.length <= m * n` 
    - `guards[i].length == walls[j].length == 2` 
    - `0 <= row_i, row_j < m` 
    - `0 <= col_i, col_j < n` 
    - All the positions in `guards` and `walls` are **unique**.
"""

import unittest
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        # Fill in the guards and walls in the grid
        # - 1 for guard
        # - 2 for wall
        for x, y in guards:
            grid[x][y] = 1
        for x, y in walls:
            grid[x][y] = 2

        # Fill in the cells that are guarded
        # - 3 represents a guarded cell
        for i, j in guards:
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x, y = i, j
                while 0 <= x + dx < m \
                        and 0 <= y + dy < n \
                        and grid[x + dx][y + dy] != 1 \
                        and grid[x + dx][y + dy] != 2:
                    grid[x + dx][y + dy] = 3
                    x, y = x + dx, y + dy

        return sum([row.count(0) for row in grid])


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]), 7)

    def testcase2(self):
        self.assertEqual(self.soln_obj.countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]), 4)

    def testcase3(self):
        self.assertEqual(self.soln_obj.countUnguarded(2, 7, [[1, 5], [1, 1], [1, 6], [0, 2]], [[0, 6], [0, 3], [0, 5]]), 1)

    def testcase4(self):
        self.assertEqual(self.soln_obj.countUnguarded(6, 10, [[0, 6], [2, 2], [2, 5], [1, 2], [4, 9], [2, 9], [5, 6], [4, 6]], [[1, 5]]), 8)


if __name__ == '__main__':
    unittest.main()
