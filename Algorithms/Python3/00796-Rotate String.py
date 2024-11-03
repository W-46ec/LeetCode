
"""
# Rotate String

Given two strings `s` and `goal`, return *`true` if and only if `s` can become `goal` after some number of **shifts** on `s`*.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.
 

**Example 1:** 
```
Input: s = "abcde", goal = "cdeab"
Output: true
```

**Example 2:** 
```
Input: s = "abcde", goal = "abced"
Output: false
```

**Constraints:** 
    - `1 <= s.length, goal.length <= 100` 
    - `s` and `goal` consist of lowercase English letters.
"""

import unittest

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != goal[0]:
                i += 1
            if i < len(s) and s[i : ] == goal[ : len(s) - i] and s[ : i] == goal[len(s) - i : ]:
                return True
            i += 1
        return False


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.rotateString("abcde", "cdeab"), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.rotateString("abcde", "abced"), False)

    def testcase3(self):
        self.assertEqual(self.soln_obj.rotateString("a", "aaa"), False)

    def testcase4(self):
        self.assertEqual(self.soln_obj.rotateString("abc", "c"), False)

    def testcase5(self):
        self.assertEqual(self.soln_obj.rotateString("abc", "cab"), True)

    def testcase6(self):
        self.assertEqual(self.soln_obj.rotateString("a", "a"), True)


if __name__ == '__main__':
    unittest.main()