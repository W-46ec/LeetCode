
"""
# Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.


**Example 1:** 
```
Input: [1,2,3,4]
Output: "23:41"
```

**Example 2:** 
```
Input: [5,5,5,5]
Output: ""
```

**Note:** 
    1. `A.length == 4` 
    2. `0 <= A[i] <= 9` 
"""

from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        valid = []
        for x, y, u, v in permutations(A):
            hour, minute = 10 * x + y, 10 * u + v
            if 0 <= hour and hour <= 23 and 0 <= minute and minute <= 59:
                valid.append([str(hour).zfill(2) + ':' + str(minute).zfill(2), 60 * hour + minute])
        return max(valid, key = lambda x: x[1])[0] if valid else ""

print(Solution().largestTimeFromDigits([1, 2, 3, 4]))   # "23:41"
print(Solution().largestTimeFromDigits([5, 5, 5, 5]))   # ""

