
"""
# Split a String Into the Max Number of Unique Substrings

Given a string `s`, return *the maximum number of unique substrings that the given string can be split into*.

You can split string `s` into any list of **non-empty substrings**, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are **unique**.

A **substring** is a contiguous sequence of characters within a string.


**Example 1:** 
```
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
```

**Example 2:** 
```
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
```

**Example 3:** 
```
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
```

**Constraints:** 
    `1 <= s.length <= 16` 
    `s` contains only lower case English letters.
"""

import unittest

class Solution:
    def __init__(self):
        self.seen = set()
        self.ans = 1

    def solve(self, i = 0, curr_num = 0):
            if i >= len(self.s):
                self.ans = max(self.ans, curr_num)
            for j in range(i + 1, len(self.s) + 1):
                sub_str = self.s[i : j]
                if sub_str not in self.seen:
                    self.seen.add(sub_str)
                    self.solve(j, curr_num + 1)
                    self.seen.remove(sub_str)

    def maxUniqueSplit(self, s: str) -> int:
        self.s = s
        self.solve()
        return self.ans


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.maxUniqueSplit("ababccc"), 5)

    def testcase2(self):
        self.assertEqual(self.soln_obj.maxUniqueSplit("aba"), 2)

    def testcase3(self):
        self.assertEqual(self.soln_obj.maxUniqueSplit("aa"), 1)

    def testcase4(self):
        self.assertEqual(self.soln_obj.maxUniqueSplit("abcdefgghhh"), 9)


if __name__ == '__main__':
    unittest.main()
