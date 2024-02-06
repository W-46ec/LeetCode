
"""
# Group Anagrams

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


**Example 1:** 
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:** 
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:** 
```
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints:** 
    - `1 <= strs.length <= 10^4` 
    - `0 <= strs[i].length <= 100` 
    - `strs[i]` consists of lowercase English letters.
"""

import unittest
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))] += [s]
        return anagrams.values()


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        ans = sorted([sorted(lst) for lst in [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]])
        res = sorted([sorted(lst) for lst in self.soln_obj.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])])
        self.assertEqual(ans, res)

    def testcase2(self):
        ans = sorted([sorted(lst) for lst in [[""]]])
        res = sorted([sorted(lst) for lst in self.soln_obj.groupAnagrams([""])])
        self.assertEqual(ans, res)

    def testcase3(self):
        ans = sorted([sorted(lst) for lst in [["a"]]])
        res = sorted([sorted(lst) for lst in self.soln_obj.groupAnagrams(["a"])])
        self.assertEqual(ans, res)


if __name__ == '__main__':
    unittest.main()
