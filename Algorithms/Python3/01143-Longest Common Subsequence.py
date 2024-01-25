
"""
# Longest Common Subsequence

Given two strings `text1` and `text2`, return *the length of their longest **common subsequence***. If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    - For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.


**Example 1:** 
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

**Example 2:** 
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

**Example 3:** 
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

**Constraints:** 
    - `1 <= text1.length, text2.length <= 1000` 
    - `text1` and `text2` consist of only lowercase English characters.
"""

import unittest

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j] <- LCS of text1[ : i] and text2[ : j], 
                    where 0 <= i <= len(text1), 0 <= j <= len(text2)
        Let dp[i][0] and dp[0][j] be 0, for all i, j.

        Iterate through all i = 1, 2, ..., len(text1) and j = 1, 2, ..., len(text2).

        Case 1:
        If text1[i] is equal to text2[j], it is equivalent to appending the same
        character to both of text1[ : i] and text2[ : j]. Therefore, dp[i][j] 
        shoule be equal to 1 + dp[i - 1][j - 1].

        Case 2:
        If text1[i] is NOT equal to text2[j], we will need to decide which
        character to discard. If we wanna discard text1[i], then the result will
        be equal to dp[i - 1][j]. If we discard text2[j], the result will be equal 
        to dp[i][j - 1]. Choose the one that yields the maximum value.
        """
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.longestCommonSubsequence("abcde", "ace" ), 3)

    def testcase2(self):
        self.assertEqual(self.soln_obj.longestCommonSubsequence("abc", "abc"), 3)

    def testcase3(self):
        self.assertEqual(self.soln_obj.longestCommonSubsequence("abc", "def"), 0)

    def testcase4(self):
        self.assertEqual(self.soln_obj.longestCommonSubsequence("a", "a"), 1)

    def testcase5(self):
        self.assertEqual(self.soln_obj.longestCommonSubsequence("a", "b"), 0)


if __name__ == '__main__':
    unittest.main()
