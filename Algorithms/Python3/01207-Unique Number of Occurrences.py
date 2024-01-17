
"""
# Unique Number of Occurrences

Given an array of integers `arr`, return *`true` if the number of occurrences of each value in the array is **unique** or `false` otherwise.


**Example 1:** 
```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

**Example 2:** 
```
Input: arr = [1,2]
Output: false
```

**Example 3:** 
```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

**Constraints:** 
    - `1 <= arr.length <= 1000` 
    - `-1000 <= arr[i] <= 1000` 
"""

import unittest
from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        return len(freq.values()) == len(set(freq.values()))


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.uniqueOccurrences([1, 2, 2, 1, 1, 3]), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.uniqueOccurrences([1, 2]), False)

    def testcase3(self):
        self.assertEqual(self.soln_obj.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]), True)


if __name__ == '__main__':
    unittest.main()
