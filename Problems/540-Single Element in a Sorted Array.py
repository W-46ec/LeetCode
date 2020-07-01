
"""
# Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.


**Example 1:** 
```
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
```

**Example 2:** 
```
Input: [3,3,7,7,10,11,11]
Output: 10
```

**Note:** Your solution should run in O(log n) time and O(1) space.
"""

from typing import List
from functools import reduce

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x ^ y, nums)

print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))

