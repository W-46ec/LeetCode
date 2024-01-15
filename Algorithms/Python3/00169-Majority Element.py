
"""
# Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears **more than** `⌊ n/2 ⌋` times.

You may assume that the array is non-empty and the majority element always exist in the array.

**Example 1:** 
```
Input: [3,2,3]
Output: 3
```

**Example 2:** 
```
Input: [2,2,1,1,1,2,2]
Output: 2
```
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

print(Solution().majorityElement([3, 2, 3]))    # 3
print(Solution().majorityElement([3, 3, 4]))    # 3
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))    # 2

