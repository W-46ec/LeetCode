
"""
# Subarray Sum Equals K

Given an array of integers and an integer **k**, you need to find the total number of continuous subarrays whose sum equals to **k**.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
    1. The length of the array is in range [1, 20,000].
    2. The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m, s, ans = dict(), 0, 0
        for i in range(len(nums)):
            s += nums[i]
            if s == k:
                ans += 1
            if s - k in m:
                ans += m[s - k]
            m[s] = m[s] + 1 if s in m else 1
        return ans

print(Solution().subarraySum([1, 1, 1], 2))

