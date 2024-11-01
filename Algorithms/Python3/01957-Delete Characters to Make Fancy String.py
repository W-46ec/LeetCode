
"""
# Delete Characters to Make Fancy String

A **fancy string** is a string where no **three consecutive** characters are equal.

Given a string `s`, delete the **minimum** possible number of characters from `s` to make it **fancy**.

Return *the final string after the deletion*. It can be shown that the answer will always be **unique**.


**Example 1:** 
```
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
```

**Example 2:** 
```
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
```

**Example 3:** 
```
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s` consists only of lowercase English letters.
"""

import unittest

class Solution:
    def makeFancyString(self, s: str) -> str:
        i, lst = 0, []
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            lst += [s[i] * min(2, j - i)]
            i = j
        return "".join(lst)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.makeFancyString("leeetcode"), "leetcode")

    def testcase2(self):
        self.assertEqual(self.soln_obj.makeFancyString("aaabaaaa"), "aabaa")

    def testcase3(self):
        self.assertEqual(self.soln_obj.makeFancyString("aab"), "aab")

    def testcase4(self):
        self.assertEqual(self.soln_obj.makeFancyString("a"), "a")

    def testcase5(self):
        self.assertEqual(self.soln_obj.makeFancyString("aaaaaaaa"), "aa")


if __name__ == '__main__':
    unittest.main()
