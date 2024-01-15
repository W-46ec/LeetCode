
"""
# Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

**Example 1:** 
```
Input: 16
Output: true
```

**Example 2:** 
```
Input: 5
Output: false
```

**Follow up:** Could you solve it without loops/recursion?
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # O(1) solution
        return num in [1 << 2 * i for i in range(16)]

print(Solution().isPowerOfFour(16))		# True
print(Solution().isPowerOfFour(5))		# False
print(Solution().isPowerOfFour(1))		# True
print(Solution().isPowerOfFour(4))		# True
print(Solution().isPowerOfFour(64))		# True
print(Solution().isPowerOfFour(0))		# False
print(Solution().isPowerOfFour(-4))		# False
print(Solution().isPowerOfFour(65536))	# True

