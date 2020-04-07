
"""
# Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # i, nums = 0, sorted(nums)
        # while i < len(nums) - 1:
        #     if nums[i] == nums[i + 1]:
        #         i += 2
        #     else:
        #         return nums[i]
        # return nums[-1]
        
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)

print(Solution().singleNumber([2, 2, 1]))           # 1
print(Solution().singleNumber([4, 1, 2, 1, 2]))     # 4
