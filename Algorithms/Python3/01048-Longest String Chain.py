
"""
# Longest String Chain

You are given an array of `words` where each word consists of lowercase English letters.

`wordA` is a **predecessor** of `wordB` if and only if we can insert **exactly one** letter anywhere in `wordA` **without changing the order of the other characters** to make it equal to `wordB`.

    - For example, `"abc"` is a **predecessor** of `"abac"`, while `"cba"` is not a **predecessor** of `"bcad"`.

A **word chain** is a sequence of words `[word1, word2, ..., wordk]` with `k >= 1`, where `word1` is a **predecessor** of `word2`, `word2` is a **predecessor** of `word3`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return *the **length** of the **longest possible word chain** with words chosen from the given list of `words`.


**Example 1:** 
```
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
```

**Example 2:** 
```
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
```

**Example 3:** 
```
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
```

**Constraints:** 
    - `1 <= words.length <= 1000` 
    - `1 <= words[i].length <= 16` 
    - `words[i]` only consists of lowercase English letters.
"""

from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = len)
        dp = [1] * len(words)
        max_chain_len = 0
        for i, w in enumerate(words):
            for j in range(len(w)):
                curr_word = w[ : j] + w[j + 1 : ]
                k = i - 1
                while k >= 0 and len(curr_word) <= len(words[k]):
                    if curr_word == words[k]:
                        dp[i] = max(dp[i], 1 + dp[k])
                    k -= 1
            max_chain_len = max(max_chain_len, dp[i])
        return max_chain_len

# 4
print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))

# 5
print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))

# 1
print(Solution().longestStrChain(["abcd", "dbqca"]))

# 4
print(Solution().longestStrChain(["bdca", "bda", "ca", "dca", "a"]))
