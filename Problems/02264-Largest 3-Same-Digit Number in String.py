
"""
# Largest 3-Same-Digit Number in String

You are given a string `num` representing a large integer. An integer is **good** if it meets the following conditions:
    - It is a **substring** of `num` with length `3`.
    - It consists of only one unique digit.

Return *the **maximum good** integer as a **string** or an empty string `""` if no such integer exists*.

Note:
    - A **substring** is a contiguous sequence of characters within a string.
    - There may be **leading zeroes** in `num` or a good integer.


**Example 1:** 
```
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
```

**Example 2:** 
```
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
```

**Example 3:** 
```
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
```

**Constraints:** 
    - `3 <= num.length <= 1000` 
    - `num` only consists of digits.
"""

import unittest

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr, count, max_good_int = '', 0, ""
        for i, d in enumerate(num):
            if d == curr:
                count += 1
            else:
                curr, count = d, 1
            max_good_int = max(max_good_int, curr * 3) if count == 3 else max_good_int
        return max_good_int


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.largestGoodInteger("6777133339"), "777")

    def testcase2(self):
        self.assertEqual(self.soln_obj.largestGoodInteger("2300019"), "000")

    def testcase3(self):
        self.assertEqual(self.soln_obj.largestGoodInteger("42352338"), "")

    def testcase4(self):
        self.assertEqual(self.soln_obj.largestGoodInteger("67777133339"), "777")

    def testcase5(self):
        self.assertEqual(self.soln_obj.largestGoodInteger("6777713333999"), "999")


if __name__ == '__main__':
    unittest.main()
