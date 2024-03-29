
"""
# Fibonacci Number

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,
```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```
Given `n`, calculate `F(n)`.

**Example 1:** 
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

**Example 2:** 
```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

**Example 3:** 
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

**Constraints:** 
	- `0 <= n <= 30` 
"""

from math import sqrt

class Solution:
    def fib(self, n: int) -> int:
        # # O(n)
        # a, b = 0, 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a
    
        # O(1)
        return int((sqrt(5) / 5) * (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n))

# 1
print(Solution().fib(1))

# 1
print(Solution().fib(2))

# 2
print(Solution().fib(3))

# 3
print(Solution().fib(4))

# 5
print(Solution().fib(5))
