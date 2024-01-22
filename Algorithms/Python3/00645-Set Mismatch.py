
"""
# Set Mismatch

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another** number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return *them in the form of an array*.


**Example 1:** 
```
Input: nums = [1,2,2,4]
Output: [2,3]
```

**Example 2:** 
```
Input: nums = [1,1]
Output: [1,2]
```

**Constraints:** 
    - `2 <= nums.length <= 10^4` 
    - `1 <= nums[i] <= 10^4` 
"""

import unittest
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_sum, n = sum(nums), len(nums)
        repeated = nums_sum - sum(set(nums))
        missing = (1 + n) * n // 2 - nums_sum + repeated
        return [repeated, missing]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findErrorNums([1, 2, 2, 4]), [2, 3])

    def testcase2(self):
        self.assertEqual(self.soln_obj.findErrorNums([1, 1]), [1, 2])

    def testcase3(self):
        self.assertEqual(self.soln_obj.findErrorNums([2, 2]), [2, 1])

    def testcase4(self):
        self.assertEqual(self.soln_obj.findErrorNums([3, 2, 3, 4, 6, 5]), [3, 1])


if __name__ == '__main__':
    unittest.main()

