
"""
# Word Break

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.


**Example 1:** 
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:** 
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

**Example 3:** 
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

**Constraints:** 
    - `1 <= s.length <= 300` 
    - `1 <= wordDict.length <= 1000` 
    - `1 <= wordDict[i].length <= 20` 
    - `s` and `wordDict[i]` consist of only lowercase English letters.
    - All the strings of `wordDict` are unique.
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # If any character in s is not in any of the word in wordDict, return False
        if not set(s).issubset(set("".join(wordDict))):
            return False

        # Convert wordDict into a set to allow faster look up.
        # 'invalid_strings' stores the sub-strings of s that
        # cannot be segmented into a sequence of wordDict words.
        wordDict, invalid_strings = set(wordDict), set()

        def backtracking(s, wordDict):
            # Base case: If s is one of the words in wordDict, return True
            if s in wordDict:
                return True

            # Early stopping: If we have seen s before and s cannot be
            # segmented into a sequence of wordDict words, return False
            if s in invalid_strings:
                return False

            # Backtracking
            for w in wordDict:
                if s.startswith(w) and backtracking(s[len(w) : ], wordDict):
                    return True

            # s cannot be segmented into a sequence of wordDict words.
            # Add it to 'invalid_strings', and return False
            invalid_strings.add(s)
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


