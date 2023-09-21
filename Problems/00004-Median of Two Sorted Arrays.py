
"""
# Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.


**Example 1:** 
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:** 
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Constraints:** 
    - `nums1.length == m` 
    - `nums2.length == n` 
    - `0 <= m <= 1000` 
    - `0 <= n <= 1000` 
    - `1 <= m + n <= 2000` 
    - `-10^6 <= nums1[i], nums2[i] <= 10^6` 
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # # O((M + N)log(M + N)) solution
        # lst = sorted(nums1 + nums2)
        # return lst[len(lst) // 2] if len(lst) % 2 else \
        #   (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

        # O(M + N) solution
        # length <- the total length of the merged array
        length = len(nums1) + len(nums2)

        # Indices of the middle element(s) in the merged array
        # When 'length' is odd, len(target_pos) is 1; when 'length' is even, len(target_pos) is 2.
        target_pos = ([length // 2 - 1] if length % 2 == 0 else []) + [length // 2]

        # We do not have to go through all elements in both nums1 and nums2.
        # Reaching the middle element(s) in the merged array will be sufficient.
        i, j, k, median = 0, 0, 0, 0
        while k <= target_pos[-1]:
            x1 = nums1[i] if i < len(nums1) else float('inf')
            x2 = nums2[j] if j < len(nums2) else float('inf')
            if x1 <= x2:
                median += x1 if k in target_pos else 0
                i += 1
            else:
                median += x2 if k in target_pos else 0
                j += 1
            k += 1
        return median / len(target_pos)


# 2.0
print(Solution().findMedianSortedArrays([1, 3], [2]))

# 2.5
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))

