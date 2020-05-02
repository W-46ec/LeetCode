
"""
# Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Let s <- sum, subtract 1 when it's a 0; plus 1 when it's a 1
        If s == 0, then nums[ : currentIdx] is a solution
        If sum(nums[ : i]) == sum(nums[ : j]) != 0, then [i, j) or (i, j] is a solution
        """
        ans, s, d = 0, 0, {}
        for i in range(len(nums)):
            if nums[i] == 0:
                s -= 1
            else:
                s += 1
            if s == 0:
                ans = max(ans, i + 1)
            if s in d:
                ans = max(ans, i - d[s])
            else:
                d[s] = i
        return ans

print(Solution().findMaxLength([0, 1]))     # 2
print(Solution().findMaxLength([0, 1, 0]))  # 2
print(Solution().findMaxLength([0, 1, 1]))  # 2

