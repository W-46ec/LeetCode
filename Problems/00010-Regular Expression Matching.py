
"""
# Regular Expression Matching

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:
    - `'.'` Matches any single character.
    - `'*'` Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).


**Example 1:** 
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:** 
```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3:** 
```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

**Constraints:** 
    - `1 <= s.length <= 20` 
    - `1 <= p.length <= 20` 
    - `s` contains only lowercase English letters.
    - `p` contains only lowercase English letters, `'.'`, and `'*'`.
    - It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Reference: https://leetcode.com/problems/regular-expression-matching/solutions/3489574/c-java-python-javascript-easy-dp-solution-with-detailed-explanation-dynamic-programming/

        # Dynamic programming
        # dp <- 2D array of size (m + 1) * (n + 1)
        # dp[i][j] <- whether the first i characters of s match the first j characters of p
        #     Base case: dp[0][0] <- True and dp[0][j] <- dp[0][j - 2] if p[j - 1] is '*' for j = 1, ..., n
        #     case 1: p[j - 1] is neither '.' nor '*':
        #             dp[i][j] = dp[i - 1][j - 1] if s[i - 1] == p[j - 1]
        #     case 2: p[j - 1] is '.':
        #             dp[i][j] = dp[i - 1][j - 1]
        #     case 3: p[j - 1] is '*':
        #             1) matching at least char (i.e., s[i - 1] == p[j - 2] or p[j - 2] == '.'):
        #                dp[i][j] = dp[i - 1][j]
        #             2) does not match anything:
        #                dp[i][j] = dp[i][j - 2]

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]

# False
print(Solution().isMatch("aa", "a"))

# True
print(Solution().isMatch("aa", "a*"))

# True
print(Solution().isMatch("ab", ".*"))

# True
print(Solution().isMatch("ab", "c*ab"))

# True
print(Solution().isMatch("aaa", "ab*a*c*a"))

