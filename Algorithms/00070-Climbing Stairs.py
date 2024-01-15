
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

# # ANS:
# 1
# 2
# 3
# 5
# 8
for i in range(1, 6):
    print(Solution().climbStairs(i))
