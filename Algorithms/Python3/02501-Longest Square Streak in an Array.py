
"""
# Longest Square Streak in an Array

You are given an integer array `nums`. A subsequence of `nums` is called a **square streak** if:
    - The length of the subsequence is at least `2`, and
    - **after** sorting the subsequence, each element (except the first element) is the **square** of the previous number.

Return *the length of the **longest square streak** in `nums`, or return `-1` if there is no **square streak***.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.


**Example 1:** 
```
Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.
```

**Example 2:** 
```
Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.
```

**Constraints:** 
    - `2 <= nums.length <= 10^5` 
    - `2 <= nums[i] <= 10^5` 
"""

import unittest
from typing import List
from math import sqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums, nums_set, ans = sorted(nums), set(nums), -1
        for num in nums:
            length, x = 1, num
            while x <= sqrt(nums[-1]) and x ** 2 in nums_set:
                length, x = length + 1, x ** 2
            ans = max(ans, length) if length >= 2 else ans
        return ans


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.longestSquareStreak([4, 3, 6, 16, 8, 2]), 3)

    def testcase2(self):
        self.assertEqual(self.soln_obj.longestSquareStreak([2, 3, 5, 6, 7]), -1)

    def testcase3(self):
        self.assertEqual(self.soln_obj.longestSquareStreak([2, 4, 16, 10, 100]), 3)

    def testcase4(self):
        self.assertEqual(self.soln_obj.longestSquareStreak([4, 16, 256, 65536]), 4)


if __name__ == '__main__':
    unittest.main()
