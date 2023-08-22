
"""
# Excel Sheet Column Title

Given an integer `columnNumber`, return *its corresponding column title as it appears in an Excel sheet*.

For example:

>A -> 1
>B -> 2
>C -> 3
>...
>Z -> 26
>AA -> 27
>AB -> 28 
>...


**Example 1:** 
```
Input: columnNumber = 1
Output: "A"
```

**Example 2:** 
```
Input: columnNumber = 28
Output: "AB"
```

**Example 3:** 
```
Input: columnNumber = 701
Output: "ZY"
```

**Constraints:** 
    `1 <= columnNumber <= 2^31 - 1` 
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars, ans = "ZABCDEFGHIJKLMNOPQRSTUVWXY", ""
        while columnNumber:
            # The only special case here is when remainder is 0. It corresponds to 'Z'.
            r = columnNumber % 26
            ans = chars[r] + ans
            columnNumber -= 26 if r == 0 else 0
            columnNumber //= 26
        return ans

# A
print(Solution().convertToTitle(1))

# AB
print(Solution().convertToTitle(28))

# ZY
print(Solution().convertToTitle(701))

# AZ
print(Solution().convertToTitle(2 * 26))

# BZ
print(Solution().convertToTitle(3 * 26))

# YZ
print(Solution().convertToTitle(26 * 26))

# YYZ
print(Solution().convertToTitle(26 ** 3))
