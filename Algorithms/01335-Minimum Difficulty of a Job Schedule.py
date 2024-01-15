
"""
# Minimum Difficulty of a Job Schedule

You want to schedule a list of jobs in `d` days. Jobs are dependent (i.e To work on the `ith` job, you have to finish all the jobs `j` where `0 <= j < i`).

You have to finish **at least** one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the `d` days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array `jobDifficulty` and an integer `d`. The difficulty of the `ith` job is `jobDifficulty[i]`.

Return *the minimum difficulty of a job schedule*. If you cannot find a schedule for the jobs return `-1`.


**Example 1:** 
![1335_untitled](./img/1335_untitled.png)
```
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
```

**Example 2:** 
```
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
```

**Example 3:** 
```
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
```

**Constraints:** 
    - `1 <= jobDifficulty.length <= 300` 
    - `0 <= jobDifficulty[i] <= 1000` 
    - `1 <= d <= 10` 
"""

import unittest
from typing import List
from itertools import product

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        # dp[i][j] <- Min difficulty to finish the first (j + 1) jobs in (i + 1) days,
        #             where i = 0, 1, ..., d; and j = 0, 1, ..., n; and i <= j.
        # dp[i][j] <- -1 for all i > j.
        dp = [[float('inf')] * n for _ in range(d)]

        # Base case: d = 0 -- there is only one day.
        # We need to assign all jobs we have to the day and the difficulty
        # of the day is determined by the job with the max difficulty.
        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, jobDifficulty[i])
            dp[0][i] = curr_max

        for i, j in product(range(1, d), range(n)):
            if i > j:
                # There are more days than the number of jobs we have.
                # Impossible to find a schedule, and therefore assign -1.
                dp[i][j] = -1
            else:
                # We need to determine how many jobs to assign to the last day.
                # We have (j + 1) jobs to assign to (i + 1) days, and we can assign
                # a maximum of (j - i + 1) jobs to the last day.
                # So we simply iterate through job j to job i (backward, since the jobs
                # are dependent) and find a schedule with the best overall difficulty.
                last_day_diff = 0
                for k in range(j, i - 1, -1):
                    last_day_diff = max(last_day_diff, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + last_day_diff)

        return dp[-1][-1]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.minDifficulty([6, 5, 4, 3, 2, 1], 2), 7)

    def testcase2(self):
        self.assertEqual(self.soln_obj.minDifficulty([9, 9, 9], 4), -1)

    def testcase3(self):
        self.assertEqual(self.soln_obj.minDifficulty([1, 1, 1], 3), 3)

    def testcase4(self):
        self.assertEqual(self.soln_obj.minDifficulty([7, 1, 7, 1, 7, 1], 3), 15)


if __name__ == '__main__':
    unittest.main()
