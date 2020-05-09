
"""
# Valid Perfect Square

Given a positive integer *num*, write a function which returns True if *num* is a perfect square else False.

**Note: Do not** use any built-in library function such as `sqrt`.

Example 1:
```
Input: 16
Output: true
```

Example 2:
```
Input: 14
Output: false
```
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, j = 1, num
        while i <= j:
            mid = (i + j) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                j = mid - 1
            else:
                i = mid + 1
        return False

for i in range(1, 26):
    print(i, Solution().isPerfectSquare(i))

