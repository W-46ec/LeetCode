
"""
# Edit Distance

Given two words *word1* and *word2*, find the minimum number of operations required to convert *word1* to *word2*.

You have the following 3 operations permitted on a word:
    1. Insert a character
    2. Delete a character
    3. Replace a character

**Example 1:** 
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2:** 
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```
"""

# Reference: https://leetcode.com/problems/edit-distance/discuss/662497/Java-or-C%2B%2B-or-Python3-or-with-detailed-explanation

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return m + n
        dp = [[i for i in range(n + 1)]] + [[0] * (n + 1) for i in range(m)]
        for i in range(m + 1):
            dp[i][0] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j], 
                        dp[i][j - 1], 
                        dp[i - 1][j - 1]
                    )
        return dp[m][n]
        

print(Solution().minDistance("horse", "ros"))               # 3
print(Solution().minDistance("intention", "execution"))     # 5
print(Solution().minDistance("a", "b"))                     # 1
