
"""
# Climbing Stairs

You are climbing a stair case. It takes *n* steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1:** 
```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:** 
```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:** 
    - `1 <= n <= 45` 

**Hint #1** 
To reach nth step, what could have been your previous steps? (Think about the step sizes)
"""

import unittest

class Solution:
    def climbStairs(self, n: int) -> int:
        # Let F(n) be the solution for climbing n steps
        # In order to reach step n, we can either take 1 step from step (n - 1),
        # or take 2 steps from step (n - 2).
        # Therefore, we have the recurrence relation F(n) = F(n - 1) + F(n - 2), 
        # with base cases F(1) = 1, and F(2) = 2.

        a, b = 1, 2
        for i in range(n - 1):
            a, b = b, a + b
        return a


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()
        self.answers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903]

    def testcase1(self):
        for i in range(1, 46):
            self.assertEqual(self.soln_obj.climbStairs(i), self.answers[i - 1])


if __name__ == '__main__':
    unittest.main()
