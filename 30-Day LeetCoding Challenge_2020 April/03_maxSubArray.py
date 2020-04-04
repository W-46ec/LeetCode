
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
