
"""
# Valid Anagram

Given two strings *s* and *t*, write a function to determine if *t* is an anagram of *s*.

**Example 1:** 
```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:** 
```
Input: s = "rat", t = "car"
Output: false
```

**Note:** 
You may assume the string contains only lowercase alphabets.

**Follow up:** 
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

import unittest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.isAnagram("anagram", "nagaram"), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.isAnagram("rat", "car"), False)


if __name__ == '__main__':
    unittest.main()

