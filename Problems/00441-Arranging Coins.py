
"""
# Arranging Coins

You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k` rows where the `ith` row has exactly `i` coins. The last row of the staircase **may be** incomplete.

Given the integer `n`, return *the number of **complete rows** of the staircase you will build*.


**Example 1:** 
![441_arrangecoins1-grid](./img/441_arrangecoins1-grid.jpg)
```
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
```

**Example 2:** 
![441_arrangecoins2-grid](./img/441_arrangecoins2-grid.jpg)
```
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
```

**Constraints:** 
    - `1 <= n <= 2^31 - 1` 
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

        # # Bisection method
        # if n <= 1:
        #     return n
        # lo, hi = 1, n
        # while lo < hi:
        #     mid = (lo + hi) >> 1
        #     if mid * (mid + 1) == 2 * n:
        #         return mid
        #     elif mid * (mid + 1) < 2 * n:
        #         lo = mid + 1
        #     else:
        #         hi = mid
        # return lo - 1

        # Use formula
        return floor((-1 + sqrt(1 + 8 * n)) / 2)

print(Solution().arrangeCoins(5))   # 2
print(Solution().arrangeCoins(8))   # 3
print(Solution().arrangeCoins(0))   # 0
print(Solution().arrangeCoins(1))   # 1
