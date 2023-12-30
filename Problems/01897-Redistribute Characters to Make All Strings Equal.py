
"""
# Redistribute Characters to Make All Strings Equal

You are given an array of strings `words` (**0-indexed**).

In one operation, pick two **distinct** indices `i` and `j`, where `words[i]` is a non-empty string, and move **any** character from `words[i]` to **any** position in `words[j]`.

Return *`true` if you can make every string in `words` **equal** using **any** number of operations, and `false` otherwise*.


**Example 1:** 
```
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.
```

**Example 2:** 
```
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
```

**Constraints:** 
    - `1 <= words.length <= 100` 
    - `1 <= words[i].length <= 100` 
    - `words[i]` consists of lowercase English letters.
"""

import unittest
from typing import List
from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_freq = defaultdict(int)
        for c in "".join(words):
            char_freq[c] += 1
        return all([x % len(words) == 0 for x in char_freq.values()])


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.makeEqual(["abc", "aabc", "bc"]), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.makeEqual(["ab", "a"]), False)

    def testcase3(self):
        self.assertEqual(self.soln_obj.makeEqual(["a", "b"]), False)


if __name__ == '__main__':
    unittest.main()