
"""
# Check If Two String Arrays are Equivalent

Given two string arrays `word1` and `word2`, return `true` *if the two arrays **represent** the same string, and `false` otherwise*.

A string is **represented** by an array if the array elements concatenated **in order** forms the string.


**Example 1:** 
```
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
```

**Example 2:** 
```
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
```

**Example 3:** 
```
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
```

**Constraints:** 
    - `1 <= word1.length, word2.length <= 10^3` 
    - `1 <= word1[i].length, word2[i].length <= 10^3` 
    - `1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3` 
    - `word1[i]` and `word2[i]` consist of lowercase letters.

**Hint #1** 
Concatenate all strings in the first array into a single string in the given order, the same for the second array.

**Hint #2** 
Both arrays represent the same string if and only if the generated strings are the same.
"""

import unittest
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]), False)

    def testcase3(self):
        self.assertEqual(self.soln_obj.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]), True)


if __name__ == '__main__':
    unittest.main()


