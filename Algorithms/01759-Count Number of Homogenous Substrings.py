
"""
# Count Number of Homogenous Substrings

Given a string `s`, return *the number of **homogenous** substrings of `s`*. Since the answer may be too large, return it **modulo** `10^9 + 7`.

A string is **homogenous** if all the characters of the string are the same.

A **substring** is a contiguous sequence of characters within a string.


**Example 1:** 
```
Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
```

**Example 2:** 
```
Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
```

**Example 3:** 
```
Input: s = "zzzzz"
Output: 15
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s` consists of lowercase letters.
"""

import unittest

class Solution:
    def countHomogenous(self, s: str) -> int:
        i, j, ans, mod = 0, 0, 0, 10 ** 9 + 7
        while i < len(s):
            while j + 1 < len(s) and s[j] == s[j + 1]:
                j += 1
            ans += ((j - i + 2) * (j - i + 1) // 2) % mod
            i, j = j + 1, j + 1
        return ans


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.countHomogenous("abbcccaa"), 13)

    def testcase2(self):
        self.assertEqual(self.soln_obj.countHomogenous("xy"), 2)

    def testcase3(self):
        self.assertEqual(self.soln_obj.countHomogenous("zzzzz"), 15)


if __name__ == '__main__':
    unittest.main()

