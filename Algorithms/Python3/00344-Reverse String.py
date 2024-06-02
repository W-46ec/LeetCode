
"""
# Reverse String

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.


**Example 1:** 
```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:** 
```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).
"""

import unittest
from random import randint, choices
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        lst = ['h', 'e', 'l', 'l', 'o']
        expected = lst[::-1]
        self.soln_obj.reverseString(lst)
        self.assertEqual(lst, expected)

    def testcase2(self):
        lst = ['H', 'a', 'n', 'n', 'a', 'h']
        expected = lst[::-1]
        self.soln_obj.reverseString(lst)
        self.assertEqual(lst, expected)

    def test_random(self):
        num_tests = 100
        printable_chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        for _ in range(num_tests):
            length = randint(1, 10 ** 5)
            lst = choices(printable_chars, k = length)
            expected = lst[::-1]
            self.soln_obj.reverseString(lst)
            self.assertEqual(lst, expected)


if __name__ == '__main__':
    unittest.main()

