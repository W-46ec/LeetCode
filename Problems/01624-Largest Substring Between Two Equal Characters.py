
"""
# Largest Substring Between Two Equal Characters

Given a string `s`, return *the length of the longest substring between two equal characters, excluding the two characters*. If there is no such substring return `-1`.

A **substring** is a contiguous sequence of characters within a string.


**Example 1:** 
```
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
```

**Example 2:** 
```
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
```

**Example 3:** 
```
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
```

**Constraints:** 
    - `1 <= s.length <= 300` 
    - `s` contains only lowercase English letters.
"""

import unittest

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        lo, hi, max_len = 0, len(s) - 1, -1
        while lo < len(s):
            hi = len(s) - 1
            while lo < hi and s[lo] != s[hi]:
                hi -= 1
            max_len = max(max_len, hi - lo - 1) if s[lo] == s[hi] else max_len
            lo += 1
        return max_len


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.maxLengthBetweenEqualCharacters("aa"), 0)

    def testcase2(self):
        self.assertEqual(self.soln_obj.maxLengthBetweenEqualCharacters("abca"), 2)

    def testcase3(self):
        self.assertEqual(self.soln_obj.maxLengthBetweenEqualCharacters("cbzxy"), -1)

    def testcase4(self):
        self.assertEqual(self.soln_obj.maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"), 18)


if __name__ == '__main__':
    unittest.main()
