
"""
# Minimum ASCII Delete Sum for Two Strings

Given two strings `s1` and `s2`, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.


**Example 1:** 
```
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
```

**Example 2:** 
```
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
```

**Constraints:** 
    - `1 <= s1.length, s2.length <= 1000` 
    - `s1` and `s2` consist of lowercase English letters.
"""

from itertools import product

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Use m, n to represent the lengths of s1 and s2
        m, n = len(s1), len(s2)

        # Initialize dp
        # dp[i][j] <- the optimal solution for strings s1[ : i] and s2[ : j], 
        # where i is ranged from [0, m] and j in ranged from [0, n].
        dp = [[None] * (n + 1) for i in range(m + 1)]

        # When i is 0 and j is 0, both strings are empty.
        # No deletion is needed. Therefore, dp[0][0] is 0.
        dp[0][0] = 0

        # When j is 0, s2[ : j] is empty string.
        # We need to delete all characters from s1[ : i] to make them equal.
        # Therefore, dp[i][0] is the sum of ASCII values of s1[ : i]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        # Similarly, When i is 0, s1[ : i] is empty string.
        # We need to delete all characters from s2[ : j] to make them equal.
        # Therefore, dp[0][j] is the sum of ASCII values of s2[ : j]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # Start building the solution
        for i, j in product(range(1, m + 1), range(1, n + 1)):
            if s1[i - 1] != s2[j - 1]:
                # When s1[i - 1] is not equal to s2[j - 1], we have two options:
                #     1) Delete s1[i - 1] and keep s2[j - 1]
                #     2) Delete s2[j - 1] and keep s1[i - 1]
                # Choose the one that yields the minimum objective value.
                dp[i][j] = min(
                    ord(s1[i - 1]) + dp[i - 1][j], 
                    ord(s2[j - 1]) + dp[i][j - 1]
                )
            else:
                # When s1[i - 1] is equal to s2[j - 1], we also have two options:
                #     1) Keep both of s1[i - 1] and s2[j - 1]
                #     2) Delete both of s1[i - 1] and s2[j - 1]
                # Choose the one that yields the minimum objective value.
                dp[i][j] = min(
                    dp[i - 1][j - 1], 
                    ord(s1[i - 1]) + ord(s2[j - 1]) + dp[i - 1][j - 1]
                )

        # Return optimal solution for s1, s2
        return dp[m][n]

# 231
print(Solution().minimumDeleteSum("sea", "eat"))

# 403
print(Solution().minimumDeleteSum("delete", "leet"))
