
"""
# Count the Number of Fair Pairs

Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and `upper`, return *the number of fair pairs*.

A pair `(i, j)` is **fair** if:
    - `0 <= i < j < n`, and
    - `lower <= nums[i] + nums[j] <= upper` 


**Example 1:** 
```
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
```

**Example 2:** 
```
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
```

**Constraints:** 
    - `1 <= nums.length <= 10^5` 
    - `nums.length == n` 
    - `-10^9 <= nums[i] <= 10^9` 
    - `-10^9 <= lower <= upper <= 10^9` 
"""

import unittest
from typing import List

class Solution:
    def countPairsLessEq(self, nums: List[int], upper: int) -> int:
        """
        Count the number of pairs less than or equal to upper.
        """
        i, j, count = 0, len(nums) - 1, 0
        while i < j:
            if nums[i] + nums[j] > upper:
                j -= 1
            else:
                count += j - i
                i += 1
        return count

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Return the number of pairs <= upper minus the number of pairs < lower
        """
        nums.sort()
        return self.countPairsLessEq(nums, upper) - self.countPairsLessEq(nums, lower - 1)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6), 6)

    def testcase2(self):
        self.assertEqual(self.soln_obj.countFairPairs([1, 7, 9, 2, 5], 11, 11), 1)


if __name__ == '__main__':
    unittest.main()
