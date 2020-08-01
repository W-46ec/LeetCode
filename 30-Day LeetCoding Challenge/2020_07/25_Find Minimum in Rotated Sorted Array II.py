
"""
# Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

Find the minimum element.

The array may contain duplicates.

**Example 1:** 
```
Input: [1,3,5]
Output: 1
```

**Example 2:** 
```
Input: [2,2,2,0,1]
Output: 0
```

**Note:** 
    - This is a follow up problem to Find Minimum in Rotated Sorted Array.
    - Would allow duplicates affect the run-time complexity? How and why?
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # # Built-in function
        # return min(nums)

        # Bisection method
        # Reference: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/754104/Linear-and-Binary-Search-Algorithm-Explained-or-Diagram
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:   # nums[mid] == nums[hi]
                hi -= 1
        return nums[lo]

print(Solution().findMin([1, 3, 5]))        # 1
print(Solution().findMin([2, 2, 2, 0, 1]))  # 0

