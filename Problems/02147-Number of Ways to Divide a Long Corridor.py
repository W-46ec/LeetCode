
"""
# Number of Ways to Divide a Long Corridor

Along a long library corridor, there is a line of seats and decorative plants. You are given a **0-indexed** string `corridor` of length `n` consisting of letters `'S'` and `'P'` where each `'S'` represents a seat and each `'P'` represents a plant.

One room divider has **already** been installed to the left of index `0`, and **another** to the right of index `n - 1`. Additional room dividers can be installed. For each position between indices `i - 1` and `i` (`1 <= i <= n - 1`), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has **exactly two seats** with any number of plants. There may be multiple ways to perform the division. Two ways are **different** if there is a position with a room divider installed in the first way but not in the second way.

Return *the number of ways to divide the corridor*. Since the answer may be very large, return it **modulo** `10^9 + 7`. If there is no way, return `0`.


**Example 1:** 
![2147_1](./img/2147_1.png)
```
Input: corridor = "SSPPSPS"
Output: 3
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.
```

**Example 2:** 
![2147_2](./img/2147_2.png)
```
Input: corridor = "PPSPSP"
Output: 1
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.
```

**Example 3:** 
![2147_3](./img/2147_3.png)
```
Input: corridor = "S"
Output: 0
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
```

**Constraints:** 
    - `n == corridor.length` 
    - `1 <= n <= 10^5` 
    - `corridor[i]` is either `'S'` or `'P'`.
"""

import unittest

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Ignore all plants from the front and the end, 
        # since each section has to have exactly 2 seats.
        lo, hi = 0, len(corridor) - 1
        while lo < hi and corridor[lo] == 'P':
            lo += 1
        while lo < hi and corridor[hi] == 'P':
            hi -= 1

        ans, MOD = 1, 10 ** 9 + 7
        while lo <= hi:
            # Find two seats to form a valid section.
            seat_count = 0
            while lo <= hi and seat_count < 2:
                if corridor[lo] == 'S':
                    seat_count += 1
                lo += 1
            # If we couldn't find two seats, there's no way
            # we can form a valid section. Return 0.
            if seat_count != 2:
                return 0

            # Count the number of plants followed by the 
            # two seats we just found.
            plant_count = 0
            while lo <= hi and corridor[lo] == 'P':
                plant_count += 1
                lo += 1
            # If there are P plants, there will be (P + 1)
            # slots for us the place the divider.
            ans = (ans * (plant_count + 1)) % MOD

        return ans


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.numberOfWays("SSPPSPS"), 3)

    def testcase2(self):
        self.assertEqual(self.soln_obj.numberOfWays("PPSPSP"), 1)

    def testcase3(self):
        self.assertEqual(self.soln_obj.numberOfWays("S"), 0)

    def testcase4(self):
        self.assertEqual(self.soln_obj.numberOfWays("SS"), 1)

    def testcase5(self):
        self.assertEqual(self.soln_obj.numberOfWays("SSP"), 1)

    def testcase6(self):
        self.assertEqual(self.soln_obj.numberOfWays("SSPPSPPSPPSSP"), 9)

    def testcase7(self):
        self.assertEqual(self.soln_obj.numberOfWays("SPPPPPPPSPPPSPSSSPPPPPPPPPPPPPPPPPSPPPPPPPPPPPPPPPPSPPPPPSPSPPPPPPSPSPPSPSPPPSPSPPSSPPPPPSPPSSPP"), 0)

    def testcase8(self):
        self.assertEqual(self.soln_obj.numberOfWays("PPPP"), 0)


if __name__ == '__main__':
    unittest.main()
