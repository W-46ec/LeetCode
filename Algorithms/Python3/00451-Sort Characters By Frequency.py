
"""
# Sort Characters By Frequency

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.

Return *the sorted string*. If there are multiple answers, return *any of them*.


**Example 1:** 
```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2:** 
```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3:** 
```
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

**Constraints:** 
    - `1 <= s.length <= 5 * 10^5` 
    - `s` consists of uppercase and lowercase English letters and digits.
"""

import unittest
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        keys = sorted(freq.keys(), key = lambda x: freq[x], reverse = True)
        return "".join([c * freq[c] for c in keys])


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        res = self.soln_obj.frequencySort("tree")
        ans = "eert"
        freq_res = Counter(res)
        occurances = [freq_res[k] for k in res]
        self.assertEqual(len(res), len(ans))
        self.assertEqual(sorted(res), sorted(ans))
        for i in range(len(occurances) - 1):
            self.assertGreaterEqual(occurances[i], occurances[i + 1])

    def testcase2(self):
        res = self.soln_obj.frequencySort("cccaaa")
        ans = "aaaccc"
        freq_res = Counter(res)
        occurances = [freq_res[k] for k in res]
        self.assertEqual(len(res), len(ans))
        self.assertEqual(sorted(res), sorted(ans))
        for i in range(len(occurances) - 1):
            self.assertGreaterEqual(occurances[i], occurances[i + 1])

    def testcase3(self):
        res = self.soln_obj.frequencySort("Aabb")
        ans = "bbAa"
        freq_res = Counter(res)
        occurances = [freq_res[k] for k in res]
        self.assertEqual(len(res), len(ans))
        self.assertEqual(sorted(res), sorted(ans))
        for i in range(len(occurances) - 1):
            self.assertGreaterEqual(occurances[i], occurances[i + 1])

    def testcase4(self):
        res = self.soln_obj.frequencySort("loveleetcode")
        ans = "eeeeoollvtdc"
        freq_res = Counter(res)
        occurances = [freq_res[k] for k in res]
        self.assertEqual(len(res), len(ans))
        self.assertEqual(sorted(res), sorted(ans))
        for i in range(len(occurances) - 1):
            self.assertGreaterEqual(occurances[i], occurances[i + 1])


if __name__ == '__main__':
    unittest.main()

