
"""
# Minimize Maximum Pair Sum in Array

The **pair sum** of a pair `(a,b)` is equal to `a + b`. The **maximum pair sum** is the largest **pair sum** in a list of pairs.
    - For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

Given an array `nums` of **even** length `n`, pair up the elements of `nums` into `n / 2` pairs such that:
    - Each element of `nums` is in **exactly one** pair, and
    - The **maximum pair sum** is **minimized**.

Return *the minimized **maximum pair sum** after optimally pairing up the elements*.


**Example 1:** 
```
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
```

**Example 2:** 
```
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
```

**Constraints:** 
    - `n == nums.length` 
    - `2 <= n <= 10^5` 
    - `n` is **even**.
    - `1 <= nums[i] <= 10^5` 
"""

import unittest
from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Intuition:
        The max pair sum is likely to be determined by the max value in nums.
        In order to minimize the max pair sum, we should pair the max value
        with the min value in nums. Do the same for the rest of the elements.

        Sort nums and pair nums[i] with nums[len(nums) - i - 1] 
        for i = 0, 1, ..., (len(nums) // 2) - 1.
        """
        nums = sorted(nums)
        max_pair_sum = 0
        for i in range(len(nums) // 2):
            max_pair_sum = max(max_pair_sum, nums[i] + nums[-i - 1])
        return max_pair_sum


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.minPairSum([3, 5, 2, 3]), 7)

    def testcase2(self):
        self.assertEqual(self.soln_obj.minPairSum([3, 5, 4, 2, 4, 6]), 8)


if __name__ == '__main__':
    unittest.main()
