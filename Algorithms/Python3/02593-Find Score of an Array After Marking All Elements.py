
"""
# Find Score of an Array After Marking All Elements

You are given an array `nums` consisting of positive integers.

Starting with `score = 0`, apply the following algorithm:
    - Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
    - Add the value of the chosen integer to `score`.
    - Mark **the chosen element and its two adjacent elements if they exist**.
    - Repeat until all the array elements are marked.

Return *the score you get after applying the above algorithm*.


**Example 1:** 
```
Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.
```

**Example 2:** 
```
Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.
```

**Constraints:** 
    - `1 <= nums.length <= 10^5` 
    - `1 <= nums[i] <= 10^6` 
"""

import unittest
from typing import List
import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap, marked, score = [], [False] * len(nums), 0
        for idx, element in enumerate(nums):
            heapq.heappush(heap, (element, idx))
        while heap:
            element, idx = heapq.heappop(heap)
            if marked[idx]:
                continue
            score += element
            marked[idx] = True
            marked[max(0, idx - 1)] = True
            marked[min(len(nums) - 1, idx + 1)] = True
        return score


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findScore([2, 1, 3, 4, 5, 2]), 7)

    def testcase2(self):
        self.assertEqual(self.soln_obj.findScore([2, 3, 5, 1, 3, 2]), 5)


if __name__ == '__main__':
    unittest.main()
