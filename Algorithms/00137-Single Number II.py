
"""
# Single Number II

Given a **non-empty** array of integers, every element appears *three* times except for one, which appears exactly once. Find that single one.

**Note:** 

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:** 
```
Input: [2,2,3,2]
Output: 3
```

**Example 2:** 
```
Input: [0,1,0,1,0,1,99]
Output: 99
```
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums, i = sorted(nums), 0
        while i < len(nums) - 3 and nums[i] == nums[i + 1]:
            i += 3
        return nums[i]

print(Solution().singleNumber([2, 2, 3, 2]))
print(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]))

