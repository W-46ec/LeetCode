
"""
# Find in Mountain Array

*(This problem is an **interactive problem**.)*

You may recall that an array `arr` is a **mountain array** if and only if:
    - `arr.length >= 3` 
    - There exists some `i` with `0 < i < arr.length - 1` such that:
        - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]` 
        - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]` 

Given a mountain array `mountainArr`, return the **minimum** `index` such that `mountainArr.get(index) == target`. If such an `index` does not exist, return `-1`.

**You cannot access the mountain array directly**. You may only access the array using a `MountainArray` interface:
    - `MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).
    - `MountainArray.length()` returns the length of the array.

Submissions making more than `100` calls to `MountainArray.get` will be judged *Wrong Answer*. Also, any solutions that attempt to circumvent the judge will result in disqualification.


**Example 1:** 
```
Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
```

**Example 2:** 
```
Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
```

**Constraints:** 
    - `3 <= mountain_arr.length() <= 10^4` 
    - `0 <= target <= 10^9` 
    - `0 <= mountain_arr.get(index) <= 10^9` 
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

from typing import List

class MountainArray:
    def __init__(self, arr: List):
        self.arr = arr.copy()
        self.arr_len = len(self.arr)

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return self.arr_len


class Solution:
    def findMaxIndex(self, lo: int, hi: int, mountain_arr: 'MountainArray') -> int:
        max_idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                max_idx = mid + 1
                lo = mid + 1
            else:
                max_idx = mid
                hi = mid - 1
        return max_idx

    def binarySearch(self, lo: int, hi: int, target: int, mountain_arr: 'MountainArray', reverse: bool = False) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_val = mountain_arr.get(mid)
            if target == mid_val:
                return mid
            elif target < mid_val:
                if reverse:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if reverse:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Find the index (namely 'max_idx') of the max element (i.e., the peak) in the array.
        # And then perform binary search on arr[0 : max_idx] and arr[max_idx : ].
        lo, hi = 0, mountain_arr.length() - 1
        max_idx = self.findMaxIndex(lo, hi, mountain_arr)
        idx = self.binarySearch(lo, max_idx, target, mountain_arr, False)
        return self.binarySearch(max_idx + 1, hi, target, mountain_arr, True) if idx == -1 else idx

# 2
print(Solution().findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])))

# -1
print(Solution().findInMountainArray(3, MountainArray([0, 1, 2, 4, 2, 1])))
