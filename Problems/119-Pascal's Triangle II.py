
"""
# Pascal's Triangle II

Given a non-negative index *k* where *k* ≤ 33, return the *k*^th index row of the Pascal's triangle.

Note that the row index starts from 0.

![119_PascalTriangleAnimated2](./img/119_PascalTriangleAnimated2.gif)

In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Example:** 
```
Input: 3
Output: [1,3,3,1]
```

**Follow up:** 
Could you optimize your algorithm to use only *O(k)* extra space?
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        while rowIndex + 1:
            for j in range(len(ans) - 1):
                ans[j] = ans[j] + ans[j + 1]
            ans = [1] + ans
            rowIndex -= 1
        return ans

print(Solution().getRow(3))     # [1, 3, 3, 1]

