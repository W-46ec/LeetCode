
"""
# Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.


**Example 1:** 
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2:** 
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

**Example 3:** 
```
Input: nums = [], target = 0
Output: [-1,-1]
```

**Constraints:** 
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Perform binary-search to find the index of any occurrence of the target.
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                lo = hi = mid
                break
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        # If lo > hi, it means the target was not present in nums; Return [-1, -1].
        if lo > hi:
            return [-1, -1]
        else:
            while hi + 1 < len(nums) and nums[hi + 1] == target:
                hi += 1
            while lo - 1 >= 0 and nums[lo - 1] == target:
                lo -= 1
            return [lo, hi]

# [3, 4]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

# [-1, -1]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))

# [-1, -1]
print(Solution().searchRange([], 0))
