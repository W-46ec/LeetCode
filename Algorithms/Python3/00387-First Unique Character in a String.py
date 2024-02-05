
"""
# First Unique Character in a String

Given a string `s`, *find the first non-repeating character in it and return its index*. If it does not exist, return `-1`.


**Example 1:** 
```
Input: s = "leetcode"
Output: 0
```

**Example 2:** 
```
Input: s = "loveleetcode"
Output: 2
```

**Example 3:** 
```
Input: s = "aabb"
Output: -1
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s` consists of only lowercase English letters.
"""

import unittest
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        return -1

class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.firstUniqChar("leetcode"), 0)

    def testcase2(self):
        self.assertEqual(self.soln_obj.firstUniqChar("loveleetcode"), 2)

    def testcase3(self):
        self.assertEqual(self.soln_obj.firstUniqChar("aabb"), -1)

    def testcase4(self):
        self.assertEqual(self.soln_obj.firstUniqChar("aadadaad"), -1)


if __name__ == '__main__':
    unittest.main()

