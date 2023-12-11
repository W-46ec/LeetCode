
"""
# Element Appearing More Than 25% In Sorted Array

Given an integer array **sorted** in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.


**Example 1:** 
```
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
```

**Example 2:** 
```
Input: arr = [1,1]
Output: 1
```

**Constraints:** 
    - `1 <= arr.length <= 10^4` 
    - `0 <= arr[i] <= 10^5` 
"""

import unittest
from typing import List
from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = Counter(arr)
        for x in freq:
            if freq[x] / len(arr) > 0.25:
                return x


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]), 6)

    def testcase2(self):
        self.assertEqual(self.soln_obj.findSpecialInteger([1, 1]), 1)

    def testcase3(self):
        self.assertEqual(self.soln_obj.findSpecialInteger([1, 1, 1, 2, 3, 4, 5, 6, 7]), 1)


if __name__ == '__main__':
    unittest.main()
