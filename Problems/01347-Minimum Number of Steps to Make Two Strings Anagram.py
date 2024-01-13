
"""
# Minimum Number of Steps to Make Two Strings Anagram

You are given two strings of the same length `s` and `t`. In one step you can choose **any character** of `t` and replace it with **another character**.

Return *the minimum number of steps* to make `t` an anagram of `s`.

An **Anagram** of a string is a string that contains the same characters with a different (or the same) ordering.


**Example 1:** 
```
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
```

**Example 2:** 
```
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
```

**Example 3:** 
```
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
```

**Constraints:** 
    - `1 <= s.length <= 5 * 10^4` 
    - `s.length == t.length` 
    - `s` and `t` consist of lowercase English letters only.
"""

import unittest
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s, freq_t, ops = Counter(s), Counter(t), 0
        for x in freq_s:
            diff = freq_s[x] - freq_t[x]
            ops += diff if diff > 0 else 0
        return ops


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.minSteps("bab", "aba"), 1)

    def testcase2(self):
        self.assertEqual(self.soln_obj.minSteps("leetcode", "practice"), 5)

    def testcase3(self):
        self.assertEqual(self.soln_obj.minSteps("anagram", "mangaar"), 0)


if __name__ == '__main__':
    unittest.main()
