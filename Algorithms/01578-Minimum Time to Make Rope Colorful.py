
"""
# Minimum Time to Make Rope Colorful

Alice has `n` balloons arranged on a rope. You are given a **0-indexed** string `colors` where `colors[i]` is the color of the `ith` balloon.

Alice wants the rope to be **colorful**. She does not want **two consecutive balloons** to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it **colorful**. You are given a **0-indexed** integer array `neededTime` where `neededTime[i]` is the time (in seconds) that Bob needs to remove the `ith` balloon from the rope.

Return *the **minimum time** Bob needs to make the rope **colorful***.


**Example 1:** 
![1578_ballon1](./img/1578_ballon1.jpg)
```
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.
```

**Example 2:** 
![1578_ballon2](./img/1578_ballon2.jpg)
```
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
```

**Example 3:** 
![1578_ballon3](./img/1578_ballon3.jpg)
```
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
```

**Constraints:** 
    - `n == colors.length == neededTime.length` 
    - `1 <= n <= 10^5` 
    - `1 <= neededTime[i] <= 10^4` 
    - `colors` contains only lowercase English letters.
"""

import unittest
from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        If there are x consecutive balloons of the same color, 
        we will need to remove exactly (x - 1) balloons from them
        to make the rope "colorful". Therefore, we simply keep the
        one that needs the most amount of time and remove the rest 
        of them.
        """
        i, j, time = 0, 0, 0
        while i < len(colors):
            j = i + 1
            while j < len(colors) and colors[j] == colors[i]:
                j += 1
            time += sum(neededTime[i : j]) - max(neededTime[i : j])
            i = j
        return time


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.minCost("abaac", [1, 2, 3, 4, 5]), 3)

    def testcase2(self):
        self.assertEqual(self.soln_obj.minCost("abc", [1, 2, 3]), 0)

    def testcase3(self):
        self.assertEqual(self.soln_obj.minCost("aabaa", [1, 2, 3, 4, 1]), 2)


if __name__ == '__main__':
    unittest.main()
