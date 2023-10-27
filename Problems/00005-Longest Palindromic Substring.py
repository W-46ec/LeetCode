
"""
# Longest Palindromic Substring

Given a string `s`, return *the longest palindromic substring* in `s`.


**Example 1:** 
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:** 
```
Input: s = "cbbd"
Output: "bb"
```

**Constraints:** 
    - `1 <= s.length <= 1000` 
    - `s` consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, lo, hi):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return hi - lo - 1

        lo, hi = 0, 0
        for i, c in enumerate(s):
            max_len = max(expand(s, i, i), expand(s, i, i + 1))
            if max_len > hi - lo:
                lo = i - (max_len - 1) // 2
                hi = i + max_len // 2
        return s[lo : hi + 1]


if __name__ == '__main__':
    # aba
    print(Solution().longestPalindrome("babad"))

    # bb
    print(Solution().longestPalindrome("cbbd"))
