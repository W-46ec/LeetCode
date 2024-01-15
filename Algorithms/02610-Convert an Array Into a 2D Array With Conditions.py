
"""
# Convert an Array Into a 2D Array With Conditions

You are given an integer array `nums`. You need to create a 2D array from `nums` satisfying the following conditions:
    - The 2D array should contain only the elements of the array `nums`.
    - Each row in the 2D array contains **distinct** integers.
    - The number of rows in the 2D array should be **minimal**.

Return *the resulting array*. If there are multiple answers, return any of them.

**Note** that the 2D array can have a different number of elements on each row.


**Example 1:** 
```
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
```

**Example 2:** 
```
Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
```

**Constraints:** 
    - `1 <= nums.length <= 200` 
    - `1 <= nums[i] <= nums.length` 
"""

import unittest
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums, lst = sorted(nums), []
        for x in nums:
            isFull = True
            for s in lst:
                if x not in s:
                    s.add(x)
                    isFull = False
                    break
            if isFull:
                lst += [{x}]
        return [list(s) for s in lst]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        matrix = self.soln_obj.findMatrix([1, 3, 4, 1, 2, 3, 1])
        answer = [[1, 3, 4, 2], [1, 3], [1]]
        self.assertEqual(len(matrix), len(answer))
        for i in range(len(matrix)):
            self.assertEqual(sorted(matrix[i]), sorted(answer[i]))

    def testcase2(self):
        matrix = self.soln_obj.findMatrix([1, 2, 3, 4])
        answer = [[4, 3, 2, 1]]
        self.assertEqual(len(matrix), len(answer))
        for i in range(len(matrix)):
            self.assertEqual(sorted(matrix[i]), sorted(answer[i]))


if __name__ == '__main__':
    unittest.main()
