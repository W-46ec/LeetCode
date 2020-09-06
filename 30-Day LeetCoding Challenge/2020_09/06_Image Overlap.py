
"""
# Image Overlap

Two images `A` and `B` are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image. After, the *overlap* of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does **not** include any kind of rotation.)

What is the largest possible overlap?

**Example 1:** 
```
Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
```

**Notes:** 
    1. `1 <= A.length = A[0].length = B.length = B[0].length <= 30` 
    2. `0 <= A[i][j], B[i][j] <= 1` 
"""

from typing import List

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        length, ans = len(A), 0
        for i in range(length):
            for j in range(length):
                count1, count2 = 0, 0
                for x in range(i, length):
                    for y in range(j, length):
                        if A[x][y] + B[x - i][y - j] == 2:
                            count1 += 1
                        if A[x - i][y - j] + B[x][y] == 2:
                            count2 += 1
                ans = max(ans, count1, count2)
        return ans

# 3
print(Solution().largestOverlap([
    [1, 1, 0], 
    [0, 1, 0], 
    [0, 1, 0]
], [
    [0, 0, 0], 
    [0, 1, 1], 
    [0, 0, 1]
]))

