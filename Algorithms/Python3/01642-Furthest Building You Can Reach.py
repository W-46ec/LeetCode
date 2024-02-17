
"""
# Furthest Building You Can Reach

You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`.

You start your journey from building `0` and move to the next building by possibly using bricks or ladders.

While moving from building `i` to building `i+1` (**0-indexed**),
    - If the current building's height is **greater than or equal** to the next building's height, you do **not** need a ladder or bricks.
    - If the current building's height is **less than** the next building's height, you can either use **one ladder** or (`h[i+1] - h[i]`) **bricks**.

Return *the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally*.


**Example 1:** 
![1642_q4](./img/1642_q4.jif)
```
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
```

**Example 2:** 
```
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
```

**Example 3:** 
```
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
```

**Constraints:** 
    - `1 <= heights.length <= 10^5` 
    - `1 <= heights[i] <= 10^6` 
    - `0 <= bricks <= 10^9` 
    - `0 <= ladders <= heights.length` 
"""

import unittest
from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Intuitively, we want to use ladders when we are far away from the next building, 
        and use bricks if we are close to the next building (assuming we are climbing up).

        The idea here is to always use bricks first until we don't have enough bricks to
        go further. And then ask yourself: which previous step you could have used a ladder 
        instead so that you can end up with more bricks? Choose the step that consumed the
        most of your bricks, and replace those bricks with a ladder. Now you loose a ladder
        but have more bricks to explore further. Repeat the above procedure until you can't
        go any further.

        A max heap can be used to record the number of bricks you use at each step, so that
        you can efficiently know which step consumed the most of your bricks.
        """
        curr_building, heap = 0, []
        while curr_building < len(heights) - 1:
            diff = heights[curr_building + 1] - heights[curr_building]
            if diff > 0:
                # If we have enough bricks, use the bricks first.
                if bricks >= diff:
                    bricks -= diff
                    heapq.heappush(heap, -diff)
                    curr_building += 1
                else:   # Ran out of bricks
                    # If we still have ladders, we may decide if
                    # we wanna use one in the current step and get
                    # to the next building, or we wanna use one to
                    # trade for some bricks from the previous step.
                    if ladders:
                        if heap:
                            if diff < -heap[0]:
                                bricks -= heapq.heappop(heap)
                            else:
                                curr_building += 1
                        else:
                            curr_building += 1
                        ladders -= 1
                    else:
                        break
            else:
                curr_building += 1
        return curr_building


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1), 4)

    def testcase2(self):
        self.assertEqual(self.soln_obj.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2), 7)

    def testcase3(self):
        self.assertEqual(self.soln_obj.furthestBuilding([14, 3, 19, 3], 17, 0), 3)

    def testcase4(self):
        self.assertEqual(self.soln_obj.furthestBuilding([1, 13, 1, 1, 13, 5, 11, 11], 10, 8), 7)


if __name__ == '__main__':
    unittest.main()

