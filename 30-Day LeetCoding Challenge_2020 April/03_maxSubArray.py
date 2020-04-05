
"""
Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return None
        currentMax = nums[0]
        currentSum = nums[0]
        for i in range(1, len(nums)):
            if currentSum < 0:
                # The sub-array always starts with positive number (if there's any)
                # Otherwise, you can always get a better solution by excluding those
                # negative values in the front.
                currentSum = nums[i]
            else:
                currentSum += nums[i]
            currentMax = max(currentMax, currentSum)
        return currentMax

print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
