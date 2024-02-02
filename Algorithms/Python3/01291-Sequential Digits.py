
"""
# Sequential Digits

An integer has *sequential digits* if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequential digits.


**Example 1:** 
```
Input: low = 100, high = 300
Output: [123,234]
```

**Example 2:** 
```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

**Constraints:** 
    - `10 <= low <= high <= 10^9` 
"""

import unittest
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = []
        # Start digit is ranged from 1 to 9 (inclusive)
        for start_digit in range(1, 10):
            curr_num = 0
            # End digit is ranged from start_digit to 9 (inclusive)
            for end_digit in range(start_digit, 10):
                curr_num = curr_num * 10 + end_digit
                # Add the number to nums if it is in range [low, high]
                if low <= curr_num <= high:
                    nums += [curr_num]
                elif high < curr_num:
                    break
        return sorted(nums)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.sequentialDigits(100, 300), [123, 234])

    def testcase2(self):
        self.assertEqual(self.soln_obj.sequentialDigits(1000, 13000), [1234, 2345, 3456, 4567, 5678, 6789, 12345])


if __name__ == '__main__':
    unittest.main()

