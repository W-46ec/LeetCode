
"""
# Pow(x, n)

Implement pow(*x, n*), which calculates *x* raised to the power *n* (x^n).

**Example 1:** 
```
Input: 2.00000, 10
Output: 1024.00000
```

**Example 2:** 
```
Input: 2.10000, 3
Output: 9.26100
```

**Example 3:** 
```
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

**Note:** 
    - -100.0 < *x* < 100.0
    - *n* is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

print(Solution().myPow(2.00000, 10))    # 1024.0
print(Solution().myPow(2.10000, 3))     # 9.26100
print(Solution().myPow(2.00000, -2))    # 0.25

