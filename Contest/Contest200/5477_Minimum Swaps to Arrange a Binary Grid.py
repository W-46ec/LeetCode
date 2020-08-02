
"""
# Minimum Swaps to Arrange a Binary Grid

Given an `n x n` binary `grid`, in one step you can choose two **adjacent rows** of the grid and swap them.

A grid is said to be **valid** if all the cells above the main diagonal are **zeros**.

Return *the minimum number of steps* needed to make the grid valid, or **-1** if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell `(1, 1)` and ends at cell `(n, n)`.


**Example 1:** 
![5477_1_fw](./img/5477_1_fw.jpg)
```
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
```

**Example 2:** 
![5477_2_e2](./img/5477_2_e2.jpg)
```
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
```

**Example 3:** 
![5477_3_e3](./img/5477_3_e3.jpg)
```
Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
```

**Constraints:** 
    - `n == grid.length` 
    - `n == grid[i].length` 
    - `1 <= n <= 200` 
    - `grid[i][j]` is `0` or `1` 
"""

from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            if all(map(lambda x: x == 0, grid[i][i + 1 : ])):
                continue
            swapped = False
            for j in range(i + 1, len(grid)):
                if all(map(lambda x: x == 0, grid[j][i + 1 : ])):
                    grid.insert(i, grid.pop(j))
                    count += j - i
                    swapped = True
                    break
            if not swapped:
                return -1
        return count

# 3
print(Solution().minSwaps([
    [0, 0, 1], 
    [1, 1, 0], 
    [1, 0, 0]
]))

# -1
print(Solution().minSwaps([
    [0, 1, 1, 0], 
    [0, 1, 1, 0], 
    [0, 1, 1, 0], 
    [0, 1, 1, 0]
]))

# 0
print(Solution().minSwaps([
    [1, 0, 0], 
    [1, 1, 0], 
    [1, 1, 1]
]))

# 16
print(Solution().minSwaps([
    [1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 1, 0, 1, 1], 
    [0, 1, 1, 1, 1, 1, 1, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 1, 0, 1, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0, 0, 0]
]))

