
"""
# Diagonal Traverse II

Given a 2D integer array `nums`, return *all elements of `nums` in diagonal order as shown in the below images*.


**Example 1:** 
![1424_sample_1_1784](./img/1424_sample_1_1784.png)
```
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
```

**Example 2:** 
![1424_sample_2_1784](./img/1424_sample_2_1784.png)
```
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

**Constraints:** 
    - `1 <= nums.length <= 10^5` 
    - `1 <= nums[i].length <= 10^5` 
    - `1 <= sum(nums[i].length) <= 10^5` 
    - `1 <= nums[i][j] <= 10^5` 
"""

import unittest
from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i + j] = [nums[i][j]] + d[i + j]
        return [x for k in d for x in d[k]]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 4, 2, 7, 5, 3, 8, 6, 9])

    def testcase2(self):
        self.assertEqual(self.soln_obj.findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]), [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16])


if __name__ == '__main__':
    unittest.main()