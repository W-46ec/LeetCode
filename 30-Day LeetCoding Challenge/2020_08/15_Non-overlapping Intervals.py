
"""
# Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


**Example 1:** 
```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```

**Example 2:** 
```
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```

**Example 3:** 
```
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

**Note:** 
    1. You may assume the interval's end point is always bigger than its start point.
    2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

# Reference: https://leetcode.com/problems/non-overlapping-intervals/discuss/793763/Python-Clean-code-with-concise-explanation

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals, ans, hi = sorted(intervals), 0, float('-inf')
        for l, r in intervals:
            if l < hi:
                ans += 1
                if r > hi:
                    continue
            hi = r
        return ans

# 0
print(Solution().eraseOverlapIntervals([[1, 2]]))

# 2
print(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))

# 0
print(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]))

# 2
print(Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]))

# 0
print(Solution().eraseOverlapIntervals([]))

# 2
print(Solution().eraseOverlapIntervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))


