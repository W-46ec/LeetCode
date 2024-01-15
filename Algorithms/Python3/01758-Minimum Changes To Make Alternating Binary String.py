
"""
# Minimum Changes To Make Alternating Binary String

You are given a string `s` consisting only of the characters `'0'` and `'1'`. In one operation, you can change any `'0'` to `'1'` or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string `"010"` is alternating, while the string `"0100"` is not.

Return *the **minimum** number of operations needed to make `s` alternating*.


**Example 1:** 
```
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
```

**Example 2:** 
```
Input: s = "10"
Output: 0
Explanation: s is already alternating.
```

**Example 3:** 
```
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
```

**Constraints:** 
    - `1 <= s.length <= 10^4` 
    - `s[i]` is either `'0'` or `'1'`.
"""

import unittest

class Solution:
    def minOperations(self, s: str) -> int:
        count1, count2 = 0, 0
        for i, d in enumerate(s):
            count1 += 1 if i % 2 == int(d) else 0
            count2 += 1 if (i + 1) % 2 == int(d) else 0
        return min(count1, count2)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.minOperations("0100"), 1)

    def testcase2(self):
        self.assertEqual(self.soln_obj.minOperations("10"), 0)

    def testcase3(self):
        self.assertEqual(self.soln_obj.minOperations("1111"), 2)

    def testcase4(self):
        self.assertEqual(self.soln_obj.minOperations("011001100110"), 6)


if __name__ == '__main__':
    unittest.main()