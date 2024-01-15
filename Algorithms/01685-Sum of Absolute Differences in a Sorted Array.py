
"""
# Sum of Absolute Differences in a Sorted Array

You are given an integer array `nums` sorted in **non-decreasing** order.

Build and return *an integer array `result` with the same length as `nums` such that `result[i]` is equal to the **summation of absolute differences** between `nums[i]` and all the other elements in the array*.

In other words, `result[i]` is equal to `sum(|nums[i]-nums[j]|)` where `0 <= j < nums.length` and `j != i` (**0-indexed**).


**Example 1:** 
```
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
```

**Example 2:** 
```
Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
```

**Constraints:** 
    - `2 <= nums.length <= 10^5` 
    - `1 <= nums[i] <= nums[i + 1] <= 10^4` 
"""

import unittest
from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Assume the integer sequence (i.e., nums) is given by the following: a_0 <= a_1 <= a_2 <= ... , <= a_{n - 1}.

        By definition, we have: result[i] = sum(|a_i - a_j|), for j = 0, 1, 2, .., n - 1.

        sum(|a_i - a_j|) = (a_i - a_0) + (a_i - a_1) + ... + (a_i - a_i) + (a_{i + 1} - a_i) + ... + (a_{n - 1} - a_i)
                         = [n * a_i - 2 * (n - i) * a_i] + sum(nums) - 2 * sum({a_0, a_1, ..., a_i})
                         = (2 * i - n) * a_i + sum(nums) - 2 * sum({a_0, a_1, ..., a_i})
        """
        n, prefix_sum, arr_sum = len(nums), 0, sum(nums)
        ans = [0] * n
        for i, a_i in enumerate(nums):
            ans[i] = (2 * i - n) * a_i + arr_sum - 2 * prefix_sum
            prefix_sum += a_i
        return ans


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.getSumAbsoluteDifferences([2, 3, 5]), [4, 3, 5])

    def testcase2(self):
        self.assertEqual(self.soln_obj.getSumAbsoluteDifferences([1, 4, 6, 8, 10]), [24, 15, 13, 15, 21])


if __name__ == '__main__':
    unittest.main()