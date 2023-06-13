
"""
# Equal Row and Column Pairs

Given a **0-indexed** `n x n` integer matrix `grid`, *return the number of pairs `(ri, cj)` such that row `ri` and column `cj` are equal*.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


**Example 1:** 
!(2352_ex1)[./img/2352_ex1.jpg]
```
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
```

**Example 2:** 
!(2352_ex2)[./img/2352_ex2.jpg]
```
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
```

**Constraints:** 
    - `n == grid.length == grid[i].length` 
    - `1 <= n <= 200` 
    - `1 <= grid[i][j] <= 10^5` 
"""

from typing import List
from functools import reduce

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [reduce(lambda x, y: x * 10 + y, r) for r in grid]
        cols = [reduce(lambda x, y: x * 10 + y, r) for r in zip(*grid)]
        return sum([x == y for x in rows for y in cols])

# 1
print(Solution().equalPairs([
    [3, 2, 1], 
    [1, 7, 6], 
    [2, 7, 7]
]))

# 3
print(Solution().equalPairs([
    [3, 1, 2, 2], 
    [1, 4, 4, 5], 
    [2, 4, 2, 2], 
    [2, 4, 2, 2]
]))
