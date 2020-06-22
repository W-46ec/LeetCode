
"""
# Longest Duplicate Substring

Given a string `S`, consider all *duplicated substrings*: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return **any** duplicated substring that has the longest possible length.  (If `S` does not have a duplicated substring, the answer is `""`.)


**Example 1:** 
```
Input: "banana"
Output: "ana"
```

**Example 2:** 
```
Input: "abcd"
Output: ""
```

**Note:** 
    - 1. `2 <= S.length <= 10^5` 
    - 2. `S` consists of lowercase English letters.
"""


# Reference: https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/Python-Binary-search-O(n-log-n)-average-with-Rabin-Karp-explained

from collections import defaultdict

class Solution:
    def RabinKarp(self,text, M, q):
        if M == 0:
            return True
        h, t, d = (1 << (8 * M - 8)) % q, 0, 256
        dic = defaultdict(list)
        for i in range(M): 
            t = (d * t + ord(text[i])) % q
        dic[t].append(i - M + 1)
        for i in range(len(text) - M):
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            for j in dic[t]:
                if text[i + 1 : i + M + 1] == text[j : j + M]:
                    return (True, text[j : j + M])
            dic[t].append(i + 1)
        return (False, "")

    def longestDupSubstring(self, S: str) -> str:
        beg, end = 0, len(S)
        q = (1 << 31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end) // 2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid
        return Found

print(Solution().longestDupSubstring("banana"))
print(Solution().longestDupSubstring("abcd"))
