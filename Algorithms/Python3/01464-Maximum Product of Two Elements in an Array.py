
"""
# Maximum Product of Two Elements in an Array

Given the array of integers `nums`, you will choose two different indices `i` and `j` of that array. *Return the maximum value of `(nums[i]-1)*(nums[j]-1)`*.


**Example 1:** 
```
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
```

**Example 2:** 
```
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
```

**Example 3:** 
```
Input: nums = [3,7]
Output: 12
```

**Constraints:** 
    - `2 <= nums.length <= 500` 
    - `1 <= nums[i] <= 10^3` 
"""

import unittest
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # O(n^2)
        # max_prod = float('-inf')
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         max_prod = max(max_prod, (nums[i] - 1) * (nums[j] - 1))
        # return max_prod

        # O(n * log n)
        nums = sorted(nums)
        return (nums[-1] - 1) * (nums[-2] - 1)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.maxProduct([3, 4, 5, 2]), 12)

    def testcase2(self):
        self.assertEqual(self.soln_obj.maxProduct([1, 5, 4, 5]), 16)

    def testcase3(self):
        self.assertEqual(self.soln_obj.maxProduct([3, 7]), 12)


if __name__ == '__main__':
    unittest.main()
