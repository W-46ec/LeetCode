
"""
# Longest Increasing Subsequence

Given an integer array `nums`, return *the length of the longest **strictly increasing** subsequence*.


**Example 1:** 
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:** 
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:** 
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

**Constraints:** 
    - `1 <= nums.length <= 2500` 
    - `-10^4 <= nums[i] <= 10^4` 


**Follow up**: Can you come up with an algorithm that runs in `O(n log(n))` time complexity?
"""

import unittest
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, LIS_len = [1] * len(nums), 0
        for i in range(len(nums)):
            longest_prev = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    longest_prev = max(longest_prev, dp[j])
            dp[i] += longest_prev
            LIS_len = max(LIS_len, dp[i])
        return LIS_len


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def testcase2(self):
        self.assertEqual(self.soln_obj.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)

    def testcase3(self):
        self.assertEqual(self.soln_obj.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)

    def testcase4(self):
        self.assertEqual(self.soln_obj.lengthOfLIS([0]), 1)


if __name__ == '__main__':
    unittest.main()
