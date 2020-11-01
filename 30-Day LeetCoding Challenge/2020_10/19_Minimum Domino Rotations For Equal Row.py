
"""
# Minimum Domino Rotations For Equal Row

In a row of dominoes, `A[i]` and `B[i]` represent the top and bottom halves of the `ith` domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the `ith` domino, so that `A[i]` and `B[i]` swap values.

Return the minimum number of rotations so that all the values in `A` are the same, or all the values in `B` are the same.

If it cannot be done, return `-1`.


**Example 1:** 
![19_domino](./img/19_domino.png)
```
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
```

**Example 2:** 
```
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
```

**Constraints:** 
    - `2 <= A.length == B.length <= 2 * 10^4` 
    - `1 <= A[i], B[i] <= 6` 
"""

from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def scan(matrix, level, target):
            count = 0
            for i in range(len(A)):
                if matrix[0][i] != target and matrix[1][i] != target:
                    return -1
                count += 1 if matrix[level][i] != target else 0
            return count

        rotations = []
        for target in [A[0], B[0]]:
            for level in range(2):
                ret = scan([A, B], level, target)
                rotations += [ret] if ret != -1 else []
        return min(rotations) if rotations else -1

# 2
print(Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))

# -1
print(Solution().minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))

