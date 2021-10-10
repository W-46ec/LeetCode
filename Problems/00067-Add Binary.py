
"""
# Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both **non-empty** and contains only characters `1` or `0`.

**Example 1:** 
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:** 
```
Input: a = "1010", b = "1011"
Output: "10101"
```

**Constraints:** `
    - Each string consists only of `'0'` or `'1'` characters.
    - `1 <= a.length, b.length <= 10^4` 
    - Each string is either `"0"` or doesn't contain any leading zero.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, base = 2) + int(b, base = 2))[2 : ]

print(Solution().addBinary("11", "1"))          # "100"
print(Solution().addBinary("1010", "1011"))     # "10101"

