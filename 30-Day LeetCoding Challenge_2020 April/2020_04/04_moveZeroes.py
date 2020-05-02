
"""
# Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
    1. You must do this in-place without making a copy of the array.
    2. Minimize the total number of operations.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Method 1
        # i, j = 0, 0
        # while j < len(nums):
        #     if nums[j] != 0:
        #         nums[i] = nums[j]
        #         i += 1
        #     j += 1
        # while i < len(nums):
        #     nums[i] = 0
        #     i += 1

        # Method 2
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)

lst = [0, 1, 0, 3, 12]
Solution().moveZeroes(lst)
print(lst)

lst = [1, 0, 0, 0, 1]
Solution().moveZeroes(lst)
print(lst)
