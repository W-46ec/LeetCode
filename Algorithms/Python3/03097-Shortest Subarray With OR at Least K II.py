
"""
# Shortest Subarray With OR at Least K II

You are given an array `nums` of **non-negative** integers and an integer `k`.

An array is called **special** if the bitwise `OR` of all of its elements is **at least** `k`.

Return *the length of the **shortest special non-empty** subarray of `nums`, or return `-1` if no special subarray exists*.


**Example 1:** 
```
Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.
```

**Example 2:** 
```
Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.
```

**Example 3:** 
```
Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.
```

**Constraints:** 
    - `1 <= nums.length <= 2 * 10^5` 
    - `0 <= nums[i] <= 10^9` 
    - `0 <= k <= 10^9` 
"""

import unittest
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits, lo, OR_sum, ans = [0] * 32, 0, 0, len(nums) + 1
        for hi in range(len(nums)):
            # OR nums[hi]
            pos, x, OR_sum = 0, nums[hi], OR_sum | nums[hi]
            while x:
                bits[pos] += (x & 0x1)
                pos, x = pos + 1, x >> 1

            # Reverse-OR nums[lo]
            while lo <= hi and OR_sum >= k:
                ans = min(ans, hi - lo + 1)
                pos, x = 0, nums[lo]
                while x:
                    bits[pos] -= (x & 0x1)
                    if bits[pos] == 0:
                        # Set bit i to 0
                        OR_sum &= (-1 ^ (1 << pos))
                    pos, x = pos + 1, x >> 1
                lo += 1

        return ans if ans <= len(nums) else -1


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.minimumSubarrayLength([1, 2, 3], 2), 1)

    def testcase2(self):
        self.assertEqual(self.soln_obj.minimumSubarrayLength([2, 1, 8], 10), 3)

    def testcase3(self):
        self.assertEqual(self.soln_obj.minimumSubarrayLength([1, 2], 0), 1)

    def testcase4(self):
        self.assertEqual(self.soln_obj.minimumSubarrayLength([1, 2, 4], 7), 3)

    def testcase5(self):
        self.assertEqual(self.soln_obj.minimumSubarrayLength([1, 2, 32, 21], 55), 3)


if __name__ == '__main__':
    unittest.main()
