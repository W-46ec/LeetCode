
"""
# Pascal's Triangle II

Given an integer `rowIndex`, return the `rowIndexth` (**0-indexed**) row of the **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![119_PascalTriangleAnimated2](./img/119_PascalTriangleAnimated2.gif)

In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Example 1:** 
```
Input: rowIndex = 3
Output: [1,3,3,1]
```

**Example 2:** 
```
Input: rowIndex = 0
Output: [1]
```

**Example 3:** 
```
Input: rowIndex = 1
Output: [1,1]
```

**Constraints:** 
    - `0 <= rowIndex <= 33` 


**Follow up**: Could you optimize your algorithm to use only `O(rowIndex)` extra space?
"""

from typing import List
from math import comb

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # # Iterative solution
        # row = []
        # while rowIndex + 1:
        #     for j in range(len(row) - 1):
        #         row[j] = row[j] + row[j + 1]
        #     row = [1] + row
        #     rowIndex -= 1
        # return row

        # Math - Binomial theorem
        # (a + b)^n = \Sigma_{i = 0}^{n} {{n}\choose{i}} a^{i} b^{n - i}
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]

# [1]
print(Solution().getRow(0))

# [1, 1]
print(Solution().getRow(1))

# [1, 2, 1]
print(Solution().getRow(2))

# [1, 3, 3, 1]
print(Solution().getRow(3))

# [1, 4, 6, 4, 1]
print(Solution().getRow(4))
