
"""
# Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return *the `kth` largest element in the array*.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?


**Example 1:** 
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:** 
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints:** 
    - `1 <= k <= nums.length <= 10^5` 
    - `-10^4 <= nums[i] <= 10^4` 
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # With sorting
        # return sorted(nums, reverse = True)[k - 1]

        # Without sorting
        # Create a min heap for the negation of the elements in 'nums' so that the 
        # kth smallest element in the heap corresponds to the kth largest element in 'nums'.
        neg_nums = [-x for x in nums]
        heapq.heapify(neg_nums)

        # Pop the first k - 1 elements
        for _ in range(k - 1):
            heapq.heappop(neg_nums)

        # Return the negation of the kth element in the heap
        return -heapq.heappop(neg_nums)

# 5
print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))

# 4
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
