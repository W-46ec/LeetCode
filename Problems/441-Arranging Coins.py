
"""
# Arranging Coins

You have a total of *n* coins that you want to form in a staircase shape, where every *k*-th row must have exactly *k* coins.

Given *n*, find the total number of **full** staircase rows that can be formed.

*n* is a non-negative integer and fits within the range of a 32-bit signed integer.

**Example 1:** 
```
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
```

**Example 2:** 
```
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
```
"""

from math import floor, sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # # Use loop
        # i = 1
        # while n >= i:
        #     n -= i
        #     i += 1
        # return i - 1

        # Bisection method
        if n <= 1:
            return n
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) >> 1
            if mid * (mid + 1) == 2 * n:
                return mid
            elif mid * (mid + 1) < 2 * n:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1

        # # Use formula
        # return floor((-1 + sqrt(1 + 8 * n)) / 2)

print(Solution().arrangeCoins(5))   # 2
print(Solution().arrangeCoins(8))   # 3
print(Solution().arrangeCoins(0))   # 0
print(Solution().arrangeCoins(1))   # 1
