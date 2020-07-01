
"""
# Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

**Example 1:** 
```
Input: [1,3,5,6], 5
Output: 2
```

**Example 2:** 
```
Input: [1,3,5,6], 2
Output: 1
```

**Example 3:** 
```
Input: [1,3,5,6], 7
Output: 4
```

**Example 4:** 
```
Input: [1,3,5,6], 0
Output: 0
```
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return i

print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))
print(Solution().searchInsert([1, 3, 5, 6], 0))

