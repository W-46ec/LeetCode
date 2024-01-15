
"""
# Power of Two

Given an integer, write a function to determine if it is a power of two.

**Example 1:** 
```
Input: 1
Output: true 
Explanation: 20 = 1
```

**Example 2:** 
```
Input: 16
Output: true
Explanation: 24 = 16
```

**Example 3:** 
```
Input: 218
Output: false
```
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 1 and n % 2 == 0:
            n //= 2
            if n == 1:
                return True
        return False

print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(218))

