
"""
# Daily Temperatures

Given an array of integers `temperatures` represents the daily temperatures, return *an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.


**Example 1:** 
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:** 
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:** 
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Constraints:** 
    - `1 <= temperatures.length <= 10^5` 
    - `30 <= temperatures[i] <= 100` 

**Hint 1** 
If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack
        n = len(temperatures)
        stack, ans, idx = [], [0] * n, 0
        while idx < n:
            curr = temperatures[idx]
            while stack and curr > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = idx - prev_idx
            stack.append(idx)
            idx += 1
        return ans

# [1, 1, 4, 2, 1, 1, 0, 0]
print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# [1, 1, 1, 0]
print(Solution().dailyTemperatures([30, 40, 50, 60]))

# [1, 1, 0]
print(Solution().dailyTemperatures([30, 60, 90]))
