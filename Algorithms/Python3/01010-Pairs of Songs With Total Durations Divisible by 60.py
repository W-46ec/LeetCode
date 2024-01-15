
"""
# Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration of `time[i]` seconds.

Return *the number of pairs of songs for which their total duration in seconds is divisible by `60`*. Formally, we want the number of indices `i`, `j` such that `i < j` with `(time[i] + time[j]) % 60 == 0`.


**Example 1:** 
```
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
```

**Example 2:** 
```
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
```

**Constraints:** 
    - `1 <= time.length <= 6 * 10^4` 
    - `1 <= time[i] <= 500` 

**Hint 1** 
We only need to consider each song length modulo 60.

**Hint 2** 
We can count the number of songs with (length % 60) equal to r, and store that in an array of size 60.
"""

from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count, ans = defaultdict(int), 0
        for t in time:
            ans += count[60 - t % 60] if t % 60 else count[0]
            count[t % 60] += 1
        return ans

# 3
print(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40]))

# 3
print(Solution().numPairsDivisibleBy60([60, 60, 60]))
