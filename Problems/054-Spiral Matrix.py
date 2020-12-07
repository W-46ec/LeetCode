
"""
# Spiral Matrix

Given an `m x n matrix`, return *all elements of the `matrix` in spiral order*.

**Example 1:** 
![054_spiral1](./img/054_spiral1.jpg)
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:** 
![054_spiral](./img/054_spiral.jpg)
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Constraints:** 
    - `m == matrix.length` 
    - `n == matrix[i].length` 
    - `1 <= m, n <= 10` 
    - `-100 <= matrix[i][j] <= 100` 
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        lst, curr_dir, x, y = [], 0, 0, 0
        while len(lst) < m * n:
            lst, matrix[x][y] = lst + [matrix[x][y]], float('inf')
            dx, dy = directions[curr_dir][0], directions[curr_dir][1]
            if not (0 <= x + dx < m) or not (0 <= y + dy < n) or matrix[x + dx][y + dy] == float('inf'):
                curr_dir = (curr_dir + 1) % len(directions)
                dx, dy = directions[curr_dir][0], directions[curr_dir][1]
            x, y = x + dx, y + dy
        return lst

# [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(Solution().spiralOrder([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]))


# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(Solution().spiralOrder([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
]))

