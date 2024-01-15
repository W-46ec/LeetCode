
"""
# Determine if String Halves Are Alike

You are given a string `s` of even length. Split this string into two halves of equal lengths, and let `a` be the first half and `b` be the second half.

Two strings are **alike** if they have the same number of vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`, `'A'`, `'E'`, `'I'`, `'O'`, `'U'`). Notice that `s` contains uppercase and lowercase letters.

Return *`true` if `a` and `b` are **alike***. Otherwise, return `false`.


**Example 1:** 
```
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
```

**Example 2:** 
```
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
```

**Example 3:** 
```
Input: s = "MerryChristmas"
Output: false
```

**Example 4:** 
```
Input: s = "AbCdEfGh"
Output: true
```

**Constraints:** 
    - `2 <= s.length <= 1000` 
    - `s.length` is even.
    - `s` consists of **uppercase and lowercase** letters.

**Hint #1** 
Create a function that checks if a character is a vowel, either uppercase or lowercase.
"""

import unittest

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        return sum(map(lambda c: c in vowels, s[ : len(s) // 2])) == sum(map(lambda c: c in vowels, s[len(s) // 2 : ]))


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.halvesAreAlike("book"), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.halvesAreAlike("textbook"), False)

    def testcase3(self):
        self.assertEqual(self.soln_obj.halvesAreAlike("MerryChristmas"), False)

    def testcase4(self):
        self.assertEqual(self.soln_obj.halvesAreAlike("AbCdEfGh"), True)


if __name__ == '__main__':
    unittest.main()