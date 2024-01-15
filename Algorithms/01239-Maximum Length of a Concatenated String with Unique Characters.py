
"""
# Maximum Length of a Concatenated String with Unique Characters

Given an array of strings `arr`. String `s` is a concatenation of a sub-sequence of `arr` which have **unique characters**.

Return *the maximum possible length* of `s`.


**Example 1:** 
```
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
```

**Example 2:** 
```
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
```

**Example 3:** 
```
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
```

**Constraints:** 
    - `1 <= arr.length <= 16` 
    - `1 <= arr[i].length <= 26` 
    - `arr[i]` contains only lower case English letters.

**Hint #1** 
You can try all combinations and keep mask of characters you have.

**Hint #2** 
You can use DP.
"""

# Reference: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/419204/3-Solutions%3A-Backtracking-Recursive-and-DP-solutions-(With-Video-explanations)

from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        words = [set()]
        for w in arr:
            curr = set(w)
            if len(curr) == len(w):
                for i in range(len(words)):
                    if len(curr & words[i]) == 0:
                        words.append(words[i] | curr)
        return len(max(words, key = len))

# 4
print(Solution().maxLength(["un", "iq", "ue"]))

# 6
print(Solution().maxLength(["cha", "r", "act", "ers"]))

# 26
print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))

