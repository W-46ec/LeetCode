
"""
# Valid Palindrome III

Given a string `s` and an integer `k`, return `true` if `s` is a `k`-**palindrome**.

A string is `k`-**palindrome** if it can be transformed into a palindrome by removing at most `k` characters from it.

**Example 1:** 
```
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
```

**Example 2:** 
```
Input: s = "abbababa", k = 1
Output: true
```

**Constraints:** 
    - `1 <= s.length <= 1000` 
    - `s` consists of only lowercase English letters.
    - `1 <= k <= s.length` 
"""

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Calculate the minimum number of characters we need 
        # to remove from s to make s a palindrome.
        # If the number is <= k, then it is possible
        return self.min_remove(s, 0, len(s) - 1, {}) <= k

    def min_remove(self, s: str, lo: int, hi: int, dp: dict = {}) -> int:
        # dp[(lo, hi)] <- Minimum number of characters to remove
        #                 to make s[lo : hi + 1] a palindrome

        # If s is an empty string or single character,  
        # then we don't need to remove anything.
        if lo >= hi:
            return 0

        # If dp[(lo, hi)] already exists, then we don't 
        # need to recompute it
        if (lo, hi) in dp:
            return dp[(lo, hi)]

        # Case 1: If s[lo] is the same as s[hi],
        #         then dp[(lo, hi)] == dp[(lo + 1, hi - 1)]
        # Case 2: If they are different, then
        #         either remove s[lo] or s[hi]
        if s[lo] == s[hi]:
            dp[(lo, hi)] = self.min_remove(s, lo + 1, hi - 1, dp)
        else:
            dp[(lo, hi)] = 1 + min(
                self.min_remove(s, lo + 1, hi, dp), 
                self.min_remove(s, lo, hi - 1, dp)
            )
        return dp[(lo, hi)]

# True
print(Solution().isValidPalindrome("abcdeca", 2))

# True
print(Solution().isValidPalindrome("abbababa", 1))

# False
print(Solution().isValidPalindrome("bacabaaa", 2))
