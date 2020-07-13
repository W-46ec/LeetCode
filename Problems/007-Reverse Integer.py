
"""
# Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:** 
```
Input: 123
Output: 321
```

**Example 2:** 
```
Input: -123
Output: -321
```

**Example 3:** 
```
Input: 120
Output: 21
```

**Note:** 
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign, x, ans = 1 if x >= 0 else -1, abs(x), 0
        while x:
            ans = 10 * ans + x % 10
            x //= 10
        return sign * ans if ans >= -(2 ** 31) and ans < 2 ** 31 else 0

print(Solution().reverse(123))          # 321
print(Solution().reverse(-123))         # -321
print(Solution().reverse(120))          # 21
print(Solution().reverse(1534236469))   # 0

