
"""
# Integer Break

Given an integer `n`, break it into the sum of `k` **positive integers**, where `k >= 2`, and maximize the product of those integers.

Return *the maximum product you can get*.


**Example 1:** 
```
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

**Example 2:** 
```
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

**Constraints:** 
    - `2 <= n <= 58` 
"""

from functools import reduce

class Solution:
    def integerBreak(self, n: int) -> int:
        max_prod = 1
        for k in range(2, n + 1):
            lst = [n // k] * k
            for i in range(n % k):
                lst[i] += 1
            max_prod = max(max_prod, reduce(lambda x, y: x * y, lst))
        return max_prod

# [1, 2, 4, 6, 9, 12, 18, 27, 36, 54, 81, 108, 162, 243, 324, 486, 729, 972, 1458, 2187, 2916, 4374, 6561, 8748, 13122, 19683, 26244, 39366, 59049, 78732, 118098, 177147, 236196, 354294, 531441, 708588, 1062882, 1594323, 2125764, 3188646, 4782969, 6377292, 9565938, 14348907, 19131876, 28697814, 43046721, 57395628, 86093442, 129140163, 172186884, 258280326, 387420489, 516560652, 774840978, 1162261467, 1549681956]
print([Solution().integerBreak(n) for n in range(2, 59)])
