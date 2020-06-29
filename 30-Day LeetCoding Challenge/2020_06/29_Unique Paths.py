
"""
# Unique Paths

A robot is located at the top-left corner of a *m x n* grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![29_robot_maze](./img/29_robot_maze.png)

Above is a 7 x 3 grid. How many possible unique paths are there?


**Example 1:** 
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

**Example 2:** 
```
Input: m = 7, n = 3
Output: 28
```

**Constraints:** 
    - `1 <= m, n <= 100` 
    - It's guaranteed that the answer will be less than or equal to `2 * 10 ^ 9`.
"""

from math import factorial as fac

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return fac(m + n - 2) // (fac(m - 1) * fac(n - 1))

print(Solution().uniquePaths(3, 2))     # 3
print(Solution().uniquePaths(7, 3))     # 28
print(Solution().uniquePaths(1, 1))     # 1

