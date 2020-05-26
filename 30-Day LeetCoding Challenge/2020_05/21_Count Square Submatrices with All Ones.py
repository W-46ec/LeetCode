
"""
# Count Square Submatrices with All Ones

Given a `m * n` matrix of ones and zeros, return how many **square** submatrices have all ones.


**Example 1:** 
```
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```

**Example 2:** 
```
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
```

**Constraints:** 
    - `1 <= arr.length <= 300` 
    - `1 <= arr[0].length <= 300` 
    - `0 <= arr[i][j] <= 1` 
"""

from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # O(N^3)
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for k in range(min(len(matrix) - i, len(matrix[0]) - j)):
                    if sum([matrix[i + k][idx] for idx in range(j, j + k + 1)]) == k + 1 and \
                        sum([matrix[idx][j + k] for idx in range(i, i + k + 1)]) == k + 1:
                        ans += 1
                    else:
                        break
        return ans

print(Solution().countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))  # 15
print(Solution().countSquares([[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1]]))  # 6
