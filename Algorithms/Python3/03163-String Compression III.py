
"""
# String Compression III

Given a string `word`, compress it using the following algorithm:
- Begin with an empty string `comp`. While `word` is **not** empty, use the following operation:
    - Remove a maximum length prefix of `word` made of a *single character* `c` repeating **at most** 9 times.
    - Append the length of the prefix followed by `c` to `comp`.

Return the string `comp`.


**Example 1:** 
```
Input: word = "abcde"

Output: "1a1b1c1d1e"

Explanation:

Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

For each prefix, append "1" followed by the character to comp.
```

**Example 2:** 
```
Input: word = "aaaaaaaaaaaaaabb"

Output: "9a5a2b"

Explanation:

Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.

For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
For prefix "aaaaa", append "5" followed by "a" to comp.
For prefix "bb", append "2" followed by "b" to comp.
```

**Constraints:** 
    - `1 <= word.length <= 2 * 10^5` 
    - `word` consists only of lowercase English letters.
"""

import unittest

class Solution:
    def compressedString(self, word: str) -> str:
        i, comp = 0, ""
        while i < len(word):
            c, count = word[i], 1
            while i + count < len(word) and word[i + count] == c:
                count += 1
            i += count
            while count > 0:
                comp += str(min(9, count)) + c
                count -= min(9, count)
        return comp


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.compressedString("abcde"), "1a1b1c1d1e")

    def testcase2(self):
        self.assertEqual(self.soln_obj.compressedString("aaaaaaaaaaaaaabb"), "9a5a2b")

    def testcase3(self):
        self.assertEqual(self.soln_obj.compressedString("aaaaaaaaaa"), "9a1a")


if __name__ == '__main__':
    unittest.main()
