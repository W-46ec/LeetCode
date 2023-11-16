
"""
# Find Unique Binary String

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return *a binary string of length `n` that **does not appear** in `nums`. If there are multiple answers, you may return **any** of them*.


**Example 1:** 
```
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
```

**Example 2:** 
```
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
```

**Example 3:** 
```
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
```

**Constraints:** 
    - `n == nums.length` 
    - `1 <= n <= 16` 
    - `nums[i].length == n` 
    - `nums[i]` is either `'0'` or `'1'`.
    - All the strings of `nums` are **unique**.
"""

import unittest
from random import randint, sample
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in range(2 ** n):
            x = bin(i)[2 : ].zfill(n)
            if x not in nums:
                return x


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        nums = ["01", "10"]
        ans = { bin(i)[2 : ].zfill(len(nums)) for i in range(2 ** len(nums)) }
        self.assertIn(self.soln_obj.findDifferentBinaryString(nums), ans)

    def testcase2(self):
        nums = ["00", "01"]
        ans = { bin(i)[2 : ].zfill(len(nums)) for i in range(2 ** len(nums)) }
        self.assertIn(self.soln_obj.findDifferentBinaryString(["00", "01"]), ans)

    def testcase3(self):
        nums = ["111", "011", "001"]
        ans = { bin(i)[2 : ].zfill(len(nums)) for i in range(2 ** len(nums)) }
        self.assertIn(self.soln_obj.findDifferentBinaryString(["111", "011", "001"]), ans)

    def test_random(self):
        num_tests = 200
        for _ in range(num_tests):
            n = randint(1, 16)
            nums_all = [bin(i)[2 : ].zfill(n) for i in range(2 ** n)]
            nums = sample(nums_all, k = n)
            ans = set(nums_all) - set(nums)
            assert len(nums_all) == 2 ** n
            assert all(map(lambda x: len(x) == n, nums_all))
            assert len(nums) == n
            assert len(ans) + len(nums) == len(nums_all)
            self.assertIn(self.soln_obj.findDifferentBinaryString(nums), ans)


if __name__ == '__main__':
    unittest.main()

