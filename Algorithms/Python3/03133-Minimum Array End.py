
"""
# Minimum Array End

You are given two integers `n` and `x`. You have to construct an array of **positive** integers `nums` of size `n` where for every `0 <= i < n - 1`, `nums[i + 1]` is **greater than** `nums[i]`, and the result of the bitwise `AND` operation between all elements of `nums` is `x`.

Return the **minimum** possible value of `nums[n - 1]`.


**Example 1:** 
```
Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.
```

**Example 2:** 
```
Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.
```

**Constraints:** 
	- `1 <= n, x <= 10^8` 
"""

import unittest

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
        Explanation:
        Let x = (b_{l - 1}, ..., b_1, b_0) be an l-bit binary number.
        We want the bitwise AND operation between all nums[i] to be x.
        That means if the j^th bit in x is 1, the j^th bit in all of nums[i]
        has to be 1 as well, where 0 <= j < l and 0 <= i < n.

        If the k^th bit in x is 0, then we have to make sure at least one
        element from nums has a binary 0 in the k^th bit. That means among
        all elements in nums, we can have at most (n - 1) of them whose k^th
        bit is 1. That gives us 2^(n - 1) available slots to encode nums.

        We have n elements (in increasing order) to be encoded. To make the
        largest element as small as possible, we can set the first element
        to 0. Then the minimum largest element would be n - 1.
        So we just need to "write" the binary info of (n - 1) into the 
        "available slots" in x (i.e., b_k == 0 for all k >= 0).
        """
        y, offset, ans = n - 1, 0, x
        while y > 0:
            while (x >> offset) & 0x1:
                offset += 1
            y, offset, ans = y >> 1, offset + 1, ans | ((y & 0x1) << offset)
        return ans


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.minEnd(3, 4), 6)

    def testcase2(self):
        self.assertEqual(self.soln_obj.minEnd(2, 7), 15)

    def testcase3(self):
        self.assertEqual(self.soln_obj.minEnd(6715154, 7193485), 55012476815)


if __name__ == '__main__':
    unittest.main()
