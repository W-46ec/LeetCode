
"""
# Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.


**Example 1:** 
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2:** 
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Constraints:** 
    - `1 <= strs.length <= 200` 
    - `0 <= strs[i].length <= 200` 
    - `strs[i]` consists of only lower-case English letters.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for prefix in zip(*map(list, strs)):
            if all([x == prefix[0] for x in prefix]):
                ans += prefix[0]
            else:
                break
        return ans

# "fl"
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))

# ""
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
