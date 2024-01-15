
"""
# Search in Rotated Sorted Array

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of `target` if it is in `nums`, or `-1` if it is not in `nums`*.

You must write an algorithm with `O(log n)` runtime complexity.


**Example 1:** 
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:** 
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:** 
```
Input: nums = [1], target = 0
Output: -1
```

**Constraints:** 
    - `1 <= nums.length <= 5000` 
    - `-10^4 <= nums[i] <= 10^4` 
    - All values of `nums` are **unique**.
    - `nums` is an ascending array that is possibly rotated.
    - `-10^4 <= target <= 10^4` 
"""

from typing import List

class Solution:
    # Pre-conditions:
    #     - 'nums' is sorted in ascending order
    #     - 0 <= start_idx, end_idx < len(nums)
    def binary_search(self, nums: List[int], start_idx: int, end_idx: int, target: int) -> int:
        lo, hi = start_idx, end_idx
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            lo = mid + 1 if target > nums[mid] else lo
            hi = mid - 1 if target < nums[mid] else hi
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # Use binary search to find pivot k, which is the index of the smallest element in nums -- O(log n)
        lo, hi = 0, len(nums) - 1
        k, min_val = 0, nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < min_val:
                k, min_val = mid, nums[mid]
            if nums[mid] < nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1
        if nums[lo] < min_val:
            k, min_val = lo, nums[lo]

        # 'nums' can be separated into the following two sorted sub-arrays: 
        #     1) nums[0 : k]
        #     2) nums[k : ]
        # Apply binary search on the two sorted part of the array to find the target -- O(log n)
        res1 = self.binary_search(nums, 0, k, target)
        res2 = self.binary_search(nums, k, len(nums) - 1, target)

        # Overall, O(log n) + 2 * O(log n) is still O(log n) time

        return res1 if res1 != -1 else res2
            
# 4
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))

# -1
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))

# -1
print(Solution().search([1], 0))

# 1
print(Solution().search([2, 1], 1))

# 1
print(Solution().search([8, 9, 2, 3, 4], 9))
