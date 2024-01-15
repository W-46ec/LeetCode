
"""
# Find The Original Array of Prefix Xor

You are given an **integer** array `pref` of size `n`. Find and return *the array `arr` of size `n` that satisfies*:
    - `pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`.

Note that `^` denotes the **bitwise-xor** operation.

It can be proven that the answer is **unique**.


**Example 1:** 
```
Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation: From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
```

**Example 2:** 
```
Input: pref = [13]
Output: [13]
Explanation: We have pref[0] = arr[0] = 13.
```

**Constraints:** 
    - `1 <= pref.length <= 10^5` 
    - `0 <= pref[i] <= 10^6` 
"""

import unittest
from random import randint
from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        curr, arr = 0, [0] * len(pref)
        for i, x in enumerate(pref):
            arr[i] = curr ^ x
            curr ^= arr[i]
        return arr


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findArray([5, 2, 0, 3, 1]), [5, 7, 2, 3, 2])

    def testcase2(self):
        self.assertEqual(self.soln_obj.findArray([13]), [13])

    def test_random(self):
        num_tests = 10
        for _ in range(num_tests):
            pref_arr_len = randint(1, 10 ** 5)
            pref = [randint(0, 10 ** 6) for _ in range(pref_arr_len)]
            arr = self.soln_obj.findArray(pref)
            curr = 0
            for i, x in enumerate(arr):
                curr ^= x
                self.assertEqual(curr, pref[i])


if __name__ == '__main__':
    unittest.main()
