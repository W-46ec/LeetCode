
"""
# H-Index II

Given an array of citations **sorted in ascending order** (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index *h* if *h* of his/her *N* papers have **at least** *h* citations each, and the other *N − h* papers have **no more than** *h* citations each."

**Example:** 
```
Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
```

**Note:** 
    If there are several possible values for *h*, the maximum one is taken as the h-index.

**Follow up:** 
    - This is a follow up problem to H-Index, where `citations` is now guaranteed to be sorted in ascending order.
    - Could you solve it in logarithmic time complexity?
"""


# Reference: https://leetcode.com/problems/h-index-ii/discuss/693380/Python-2-Solutions%3A-binary-search-O(log-n)-and-Oneliner-O(n)-explained

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        lo, hi = 0, len(citations) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if len(citations) - mid > citations[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return len(citations) - lo

print(Solution().hIndex([0, 1, 3, 5, 6]))   # 3
print(Solution().hIndex([0]))               # 0
print(Solution().hIndex([1]))               # 1
print(Solution().hIndex([0, 0]))            # 0

