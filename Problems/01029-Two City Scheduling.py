
"""
# Two City Scheduling

There are `2N` people a company is planning to interview. The cost of flying the `i`-th person to city `A` is `costs[i][0]`, and the cost of flying the `i`-th person to city `B` is `costs[i][1]`.

Return the minimum cost to fly every person to a city such that exactly `N` people arrive in each city.


**Example 1:** 
```
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
```

**Note:** 
    1. `1 <= costs.length <= 100` 
    2. It is guaranteed that `costs.length` is even.
    3. `1 <= costs[i][0], costs[i][1] <= 1000` 
"""


# Reference: https://leetcode.com/problems/two-city-scheduling/discuss/667781/Python-3-Lines-O(n-log-n)-with-sort-explained

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Explanation: Assume I sent everybody to city A, then 
        the total cost would be `sum([x[0] for x in costs])`.
        
        However, I could have saved some money by sending some 
        of them to city B. For example, in the case `[400, 50]`, 
        I spent $400 to send that person to city A, but I could
        have saved 50 - 400 = -350 dollars by sending him to B.
        
        Therefore, if I calculate the difference (cost of B - cost of A) of
        the cost, and sort them in increasing order. Then the values in it 
        are the amount of money I cound have saved if I send them to city B.
        (Or the amount of money I have gained by sending him to A if it is positive).
        Clearly, people in the front can save me more money than the people from 
        the back.
        
        Now I just need to simply choose the first half of the people based on 
        the calculated differences, and send them to city B. And the optimal
        solution is obtained by adding the values in the first half of difference 
        array to the sum that we calculated in the previous step. Since that's 
        the amount of money I saved by sending those people to city B (If no negative
        values can be found, then this is the extra amount of money I have to pay
        in order to make sure that there are N people going to city B. But in this case
        the cost will be minimized anyway. So still optimal).
        """
        # Explanation: 
        return sum([x[0] for x in costs]) + sum(sorted([x[1] - x[0] for x in costs])[ : len(costs) // 2])


print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))  # 110

