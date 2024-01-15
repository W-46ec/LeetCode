
"""
# Merge Sorted Array

Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array.

The number of elements initialized in `nums1` and `nums2` are `m` and `n` respectively. You may assume that `nums1` has a size equal to `m + n` such that it has enough space to hold additional elements from `nums2`.


**Example 1:** 
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

**Example 2:** 
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

**Constraints:** 
    - `nums1.length == m + n` 
    - `nums2.length == n` 
    - `0 <= m, n <= 200` 
    - `1 <= m + n <= 200` 
    - `-10^9 <= nums1[i], nums2[i] <= 10^9` 

**Hint #1** 
You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?

**Hint #2** 
If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count, i, j = 0, 0, 0
        while count < m and j < n:
            if nums1[i] > nums2[j]:
                nums1[i : i] = [nums2[j]]
                nums1[m + n : m + n + 1] = []
                j += 1
            else:
                count += 1
            i += 1
        while j < n:
            nums1[i] = nums2[j]
            i, j = i + 1, j + 1


nums1 = [1, 2, 3, 0, 0, 0]
Solution().merge(nums1, 3, [2, 5, 6], 3)
print(nums1)    # [1, 2, 2, 3, 5, 6]

nums1 = [1]
Solution().merge(nums1, 1, [], 0)
print(nums1)    # [1]

# [1]
nums1 = [0]
Solution().merge(nums1, 0, [1], 1)
print(nums1)    # [1]

