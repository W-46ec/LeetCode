
"""
# Count Vowels Permutation

Given an integer `n`, your task is to count how many strings of length `n` can be formed under the following rules:
    - Each character is a lower case vowel (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`)
    - Each vowel `'a'` may only be followed by an `'e'`.
    - Each vowel `'e'` may only be followed by an `'a'` or an `'i'`.
    - Each vowel `'i'` **may not** be followed by another `'i'`.
    - Each vowel `'o'` may only be followed by an `'i'` or a `'u'`.
    - Each vowel `'u'` may only be followed by an `'a'`.

Since the answer may be too large, return it modulo `10^9 + 7`.


**Example 1:** 
```
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
```

**Example 2:** 
```
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
```

**Example 3:** 
```
Input: n = 5
Output: 68
```

**Constraints:** 
    - `1 <= n <= 2 * 10^4` 
"""

import unittest

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        Dynamic programming

        dp[c][i] <- number of strings of length (i + 1) that end with character c
                    where c is in ('a', 'e', 'i', 'o', 'u'), and i = 0, 1, ..., n - 1
        Base case: dp['a'][0] = dp['e'][0] = dp['i'][0] = dp['o'][0] = dp['u'][0] = 1
        
        By definition, we have the following relationships:
            - A character 'a' can be appended to strings end with 'e', 'i', and 'u';
            - A character 'e' can be appended to strings end with 'a', and 'i';
            - A character 'i' can be appended to strings end with 'e', and 'o';
            - A character 'o' can be appended to strings end with 'i';
            - A character 'u' can be appended to strings end with 'i', and 'o';

        Therefore, we can build the solution bottom-up and return the sum of the number of
        strings of length n that end with 'a', 'e', 'i', 'o', and 'u' respectively.

        Optimization:
        Note that at any iteration i, we only need the results from the previous iteration (i.e., i - 1).
        Therefore, we don't need an array of size O(5 * n). Instead we ony need O(5) space to store
        the results from each iteration.
        """
        dp = { c: 1 for c in "aeiou" }

        for i in range(n - 1):
            dp['a'], dp['e'], dp['i'], dp['o'], dp['u'] = \
                dp['e'] + dp['i'] + dp['u'], \
                dp['a'] + dp['i'], \
                dp['e'] + dp['o'], \
                dp['i'], \
                dp['i'] + dp['o']

        return sum(dp.values()) % (10 ** 9 + 7)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.countVowelPermutation(1), 5)

    def testcase2(self):
        self.assertEqual(self.soln_obj.countVowelPermutation(2), 10)

    def testcase3(self):
        self.assertEqual(self.soln_obj.countVowelPermutation(3), 19)

    def testcase4(self):
        self.assertEqual(self.soln_obj.countVowelPermutation(4), 35)

    def testcase5(self):
        self.assertEqual(self.soln_obj.countVowelPermutation(5), 68)

    def testcase6(self):
        self.assertEqual(self.soln_obj.countVowelPermutation(6), 129)

    def testcase7(self):
        self.assertEqual(self.soln_obj.countVowelPermutation(7), 249)

    def testcase8(self):
        self.assertEqual(self.soln_obj.countVowelPermutation(8), 474)


if __name__ == '__main__':
    unittest.main()
