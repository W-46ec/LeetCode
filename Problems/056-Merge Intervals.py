
"""
# Merge Intervals

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.


**Example 1:** 
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:** 
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**Constraints:** 
    - `1 <= intervals.length <= 10^4` 
    - `intervals[i].length == 2` 
    - `0 <= starti <= endi <= 10^4` 
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        if len(intervals) <= 1:
            return intervals
        i, length = 0, len(intervals)
        while i < length - 1:
            itvl1, itvl2 = intervals[i], intervals[i + 1]
            if itvl2[0] <= itvl1[1]:
                if itvl2[1] <= itvl1[1]:
                    intervals.pop(i + 1)
                else:
                    intervals[i + 1] = [itvl1[0], itvl2[1]]
                    intervals.pop(i)
                length -= 1
                continue
            i += 1
        return intervals

# [[1, 6], [8, 10], [15, 18]]
print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

# [[1, 5]]
print(Solution().merge([[1, 4], [4, 5]]))

# [[1, 4]]
print(Solution().merge([[1, 4], [2, 3]]))

