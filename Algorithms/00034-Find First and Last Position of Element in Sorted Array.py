
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
        # Binary Search
        # When 'first' is True, return the index of the first occurrence of the target;
        # When 'first' is False, return the index of the last occurrence of the target;
        # Return -1 if target is not present in nums.
        def binarySearch(nums: List[int], target: int, first: int = True) -> int:
            lo, hi, target_idx = 0, len(nums) - 1, -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    target_idx = mid
                    if first:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return target_idx

        return [binarySearch(nums, target, True), binarySearch(nums, target, False)]

# [3, 4]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

# [-1, -1]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))

# [-1, -1]
print(Solution().searchRange([], 0))
