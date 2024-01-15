
"""
# Perfect Squares

Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.

**Example 1:** 
```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:** 
```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```
"""

from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares, i = [], 1
        while i ** 2 <= n:
            perfect_squares.append(i ** 2)
            i += 1
        if int(sqrt(n)) ** 2 == n:
            return 1
        for x in perfect_squares:
            if n - x in perfect_squares:
                return 2
        for i in range(len(perfect_squares)):
            for j in range(len(perfect_squares)):
                if n - perfect_squares[i] - perfect_squares[j] in perfect_squares:
                    return 3
        return 4

print(Solution().numSquares(12))    # 3
print(Solution().numSquares(13))    # 2
