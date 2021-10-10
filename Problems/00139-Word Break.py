
"""
# Word Break

Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, determine if *s* can be segmented into a space-separated sequence of one or more dictionary words.

**Note:** 
    - The same word in the dictionary may be reused multiple times in the segmentation.
    - You may assume the dictionary does not contain duplicate words.

**Example 1:** 
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:** 
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

**Example 3:** 
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # # Time Limit Exceeded
        # if s == "":
        #     return True
        # for i in range(len(s)):
        #     word = s[ : i + 1]
        #     # print(word)
        #     if word != "" and word in wordDict and self.wordBreak(s[i + 1 : ], wordDict):
        #         return True
        # return False

        
        # Reference: https://leetcode.com/problems/word-break/discuss/870794/Faster-than-99.6-Python
        if any([c not in set(''.join(wordDict)) for c in s]):
            return False
        
        wordDict = sorted(wordDict, key = len, reverse = True)
        seen = set()

        def backtracking(s, wordDict):
            if s in wordDict:
                return True
            if s in seen:
                return False
            seen.add(s)
            for w in wordDict:
                if s.startswith(w) and backtracking(s[len(w) : ], wordDict):
                    return True
            return False

        return backtracking(s, wordDict)

# True
print(Solution().wordBreak("leetcode", ["leet", "code"]))

# True
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))

# False
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

# False
print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
))

# False
print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
    ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
))


