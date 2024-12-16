
"""
# Final Array State After K Multiplication Operations I

You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:
    - Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**.
    - Replace the selected minimum value `x` with `x * multiplier`.

Return an integer array denoting the *final state* of `nums` after performing all `k` operations.


**Example 1:** 
```
Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation           Result
After operation 1   [2, 2, 3, 5, 6]
After operation 2   [4, 2, 3, 5, 6]
After operation 3   [4, 4, 3, 5, 6]
After operation 4   [4, 4, 6, 5, 6]
After operation 5   [8, 4, 6, 5, 6]
```

**Example 2:** 
```
Input: nums = [1,2], k = 3, multiplier = 4

Output: [16,8]

Explanation:

Operation           Result
After operation 1   [4, 2]
After operation 2   [4, 8]
After operation 3   [16, 8]
```

Constraints:
    - `1 <= nums.length <= 100` 
    - `1 <= nums[i] <= 100` 
    - `1 <= k <= 10` 
    - `1 <= multiplier <= 5` 
"""

import unittest
from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(x, i) for i, x in enumerate(nums)]
        res = [0] * len(nums)
        heapq.heapify(heap)
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            new_val = val * multiplier
            heapq.heappush(heap, (new_val, idx))
            res[idx] = new_val
        while heap:
            val, idx = heapq.heappop(heap)
            res[idx] = val
        return res


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.getFinalState([2, 1, 3, 5, 6], 5, 2), [8, 4, 6, 5, 6])

    def testcase2(self):
        self.assertEqual(self.soln_obj.getFinalState([1, 2], 3, 4), [16, 8])


if __name__ == '__main__':
    unittest.main()
