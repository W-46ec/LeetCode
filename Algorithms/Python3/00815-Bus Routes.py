
"""
# Bus Routes

You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the `ith` bus repeats forever.
    - For example, if `routes[0] = [1, 5, 7]`, this means that the `0th` bus travels in the sequence `1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ...` forever.

You will start at the bus stop `source` (You are not on any bus initially), and you want to go to the bus stop `target`. You can travel between bus stops by buses only.

Return *the least number of buses you must take to travel from `source` to `target`*. Return `-1` if it is not possible.


**Example 1:** 
```
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
```

**Example 2:** 
```
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
```

**Constraints:** 
    - `1 <= routes.length <= 500`.
    - `1 <= routes[i].length <= 10^5` 
    - All the values of `routes[i]` are **unique**.
    - `sum(routes[i].length) <= 10^5` 
    - `0 <= routes[i][j] < 10^6` 
    - `0 <= source, target < 10^6` 
"""

import unittest
from typing import List
from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Edge case
        if source == target:
            return 0

        # Create a map that maps bus stops to route ids
        # stop2routeid[bus_stop] <- the list of routes it belongs to
        stop2routeid = defaultdict(list)
        for route_id, lst in enumerate(routes):
            for stop in lst:
                stop2routeid[stop] += [route_id]

        # Run BFS
        # Traveling between bus stops of the same route doesn't cost anything
        # Therefore, we can treat each route as a single target.
        queue = [source]
        visited_nodes, visited_routes = { source }, [False] * len(routes)
        cost = 0
        while queue:
            cost += 1
            num_stops = len(queue)
            for _ in range(num_stops):
                node = queue.pop(0)
                for route_id in stop2routeid[node]:
                    if not visited_routes[route_id]:
                        visited_routes[route_id] = True
                        for nxt_node in routes[route_id]:
                            if nxt_node == target:
                                return cost
                            queue += [nxt_node]
                            visited_nodes.add(nxt_node)
        return -1


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6), 2)

    def testcase2(self):
        self.assertEqual(self.soln_obj.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12), -1)

    def testcase3(self):
        self.assertEqual(self.soln_obj.numBusesToDestination([[1, 2, 7], [3, 6, 7], [1, 5, 3]], 1, 3), 1)


if __name__ == '__main__':
    unittest.main()
