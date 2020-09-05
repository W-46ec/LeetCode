
"""
# Partition Labels

A string `S` of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.


**Example 1:** 
```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

**Note:** 
    - `S` will have length in range `[1, 500]`.
    - `S` will consist of lowercase English letters (`'a'` to `'z'`) only.


**Hint #1** 
Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.
"""

from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans, lo, hi = [], 0, 0
        while lo < len(S):
            idx, hi = lo, S.rindex(S[lo])
            while idx < hi:
                hi = max(hi, S.rindex(S[idx]))
                idx += 1
            ans += [hi + 1] if not ans else [hi - lo + 1]
            lo = hi + 1
        return ans


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))   # [9, 7, 8]

