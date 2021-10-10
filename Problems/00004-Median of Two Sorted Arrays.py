
"""
# Median of Two Sorted Arrays

There are two sorted arrays **nums1** and **nums2** of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume **nums1** and **nums2** cannot be both empty.

**Example 1:** 
```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

**Example 2:** 
```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # # O((M + N)log(M + N)) solution
        # lst = sorted(nums1 + nums2)
        # return lst[len(lst) // 2] if len(lst) % 2 else \
        #   (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

        # O(M + N) solution
        lst = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                lst.append(nums1[i])
                i += 1
            else:
                lst.append(nums2[j])
                j += 1
        lst += nums1[i : ] if i < len(nums1) else []
        lst += nums2[j : ] if j < len(nums2) else []
        return lst[len(lst) // 2] if len(lst) % 2 else \
          (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

print(Solution().findMedianSortedArrays([1, 3], [2]))       # 2
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))    # 2.5

