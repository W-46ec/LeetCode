
"""
# Largest Odd Number in String

You are given a string `num`, representing a large integer. Return *the **largest-valued odd** integer (as a string) that is a **non-empty substring** of `num`, or an empty string `""` if no odd integer exists*.

A **substring** is a contiguous sequence of characters within a string.


**Example 1:** 
```
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
```

**Example 2:** 
```
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
```

**Example 3:** 
```
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
```

**Constraints:** 
    - `1 <= num.length <= 10^5` 
    - `num` only consists of digits and does not contain any leading zeros.
"""

import unittest

class Solution:
    def largestOddNumber(self, num: str) -> str:
        even_num, idx = {'0', '2', '4', '6', '8'}, len(num) - 1
        while idx >= 0 and num[idx] in even_num:
            idx -= 1
        return num[ : idx + 1]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.largestOddNumber("52"), "5")

    def testcase2(self):
        self.assertEqual(self.soln_obj.largestOddNumber("4206"), "")

    def testcase3(self):
        self.assertEqual(self.soln_obj.largestOddNumber("35427"), "35427")


if __name__ == '__main__':
    unittest.main()
