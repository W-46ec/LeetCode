
"""
# Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

**Example 1:** 
```
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
```

**Example 2:** 
```
Input: "aba"
Output: False
```

**Example 3:** 
```
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
```
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                if s[ : i] * (len(s) // i) == s:
                    return True
        return False

print(Solution().repeatedSubstringPattern("abab"))          # True
print(Solution().repeatedSubstringPattern("aba"))           # False
print(Solution().repeatedSubstringPattern("abcabcabcabc"))  # True
print(Solution().repeatedSubstringPattern("a"))             # False
print(Solution().repeatedSubstringPattern("bb"))            # True
print(Solution().repeatedSubstringPattern("abcabc"))        # True

