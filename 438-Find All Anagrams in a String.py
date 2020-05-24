
"""
# Find All Anagrams in a String

Given a string **s** and a **non-empty** string **p**, find all the start indices of **p**'s anagrams in **s**.

Strings consists of lowercase English letters only and the length of both strings **s** and **p** will not be larger than 20,100.

The order of output does not matter.

**Example 1:** 
```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:** 
```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```
"""

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans, i, p = [], 0, sorted(p)
        while i < len(s) - len(p) + 1:
            if s[i] in p:
                if sorted(s[i : i + len(p)]) == p:
                    ans.append(i)
                    for j in range(i + len(p), i + 2 * len(p)):
                        if j < len(s) and s[j] == s[j - len(p)]:
                            ans.append(j - len(p) + 1)
                            i += 1
                        else:
                            break
            i += 1
        return ans

print(Solution().findAnagrams("cbaebabacd", "abc"))     # [0, 6]
print(Solution().findAnagrams("abab", "ab"))            # [0, 1, 2]
print(Solution().findAnagrams("baa", "aa"))             # [1]

