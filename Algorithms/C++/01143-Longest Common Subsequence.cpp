
/*
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
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        /*
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
        */
        vector<vector<int>> dp;
        for (unsigned i = 0; i <= text1.length(); i++) {
            vector<int> row(text2.length() + 1);
            fill(row.begin(), row.end(), 0);
            dp.push_back(row);
        }

        for (unsigned i = 1; i <= text1.length(); i++) {
            for (unsigned j = 1; j <= text2.length(); j++) {
                dp[i][j] = text1[i - 1] == text2[j - 1] ? 1 + dp[i - 1][j - 1] : max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[text1.length()][text2.length()];
    }
};

int main(int argc, char *argv[]) {
    Solution obj;
    cout << obj.longestCommonSubsequence(string("abcde"), string("ace")) << endl;   // 3
    cout << obj.longestCommonSubsequence(string("abc"), string("abc")) << endl;     // 3
    cout << obj.longestCommonSubsequence(string("abc"), string("def")) << endl;     // 0
    cout << obj.longestCommonSubsequence(string("a"), string("a")) << endl;         // 1
    cout << obj.longestCommonSubsequence(string("a"), string("b")) << endl;         // 0
    return 0;
}
