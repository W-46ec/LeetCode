
"""
# Greatest Common Divisor of Strings

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return *the largest string `x` such that `x` divides both `str1` and `str2`*.


**Example 1:** 
``
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

**Example 2:** 
```
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```

**Example 3:** 
```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

**Constraints:** 
    - `1 <= str1.length, str2.length <= 1000` 
    - `str1` and `str2` consist of English uppercase letters.
"""

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # i, ans = 0, ""
        # while i < min(len(str1), len(str2)):
        #     if len(str1) % (i + 1) == 0 \
        #             and len(str2) % (i + 1) == 0 \
        #             and str1 == str1[ : i + 1] * (len(str1) // (i + 1)) \
        #             and str2 == str1[ : i + 1] * (len(str2) // (i + 1)):
        #         ans = str1[ : i + 1]
        #     i += 1
        # return ans

        return str1[ : gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""

# "ABC"
print(Solution().gcdOfStrings("ABCABC", "ABC"))

# "AB"
print(Solution().gcdOfStrings("ABABAB", "ABAB"))

# ""
print(Solution().gcdOfStrings("LEET", "CODE"))
