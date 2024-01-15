
"""
# Find All Anagrams in a String

Given two strings `s` and `p`, return *an array of all the start indices of `p`'s anagrams in `s`*. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


**Example 1:** 
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:** 
```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

**Constraints:** 
    - `1 <= s.length, p.length <= 3 * 10^4` 
    - `s` and `p` consist of lowercase English letters.
"""

from typing import List
from collections import defaultdict, Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # ans, i, p = [], 0, sorted(p)
        # while i < len(s) - len(p) + 1:
        #     if s[i] in p:
        #         if sorted(s[i : i + len(p)]) == p:
        #             ans.append(i)
        #             for j in range(i + len(p), i + 2 * len(p)):
        #                 if j < len(s) and s[j] == s[j - len(p)]:
        #                     ans.append(j - len(p) + 1)
        #                     i += 1
        #                 else:
        #                     break
        #     i += 1
        # return ans
        
        # Keep track of how many characters we need to
        # form an anagram
        needed = defaultdict(int, Counter(p))

        # Sliding window
        ans = []
        for i in range(len(s)):
            # Move the window to the right by 1 unit

            if i >= len(p):
                # On the left hand side of the window, we are
                # popping out 1 character. Therefore, the need 
                # for that character will have to increase by 1.
                needed[s[i - len(p)]] += 1

            # On the right hand side, we are adding one new
            # character. Therefore, the need for that character
            # will decrease by 1.
            needed[s[i]] -= 1

            # If at some point, we need no further characters, 
            # and have no extra characters to remove, the 
            # characters in the window form an anagram.
            if all([val == 0 for val in needed.values()]):
                ans += [i - len(p) + 1]

        return ans

# [0, 6]
print(Solution().findAnagrams("cbaebabacd", "abc"))

# [0, 1, 2]
print(Solution().findAnagrams("abab", "ab"))

# [1]
print(Solution().findAnagrams("baa", "aa"))

