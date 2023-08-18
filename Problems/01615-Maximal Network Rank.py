
"""
# Maximal Network Rank

There is an infrastructure of `n` cities with some number of `roads` connecting these cities. Each `roads[i] = [ai, bi]` indicates that there is a bidirectional road between cities `ai` and `bi`.

The **network rank** of **two different cities** is defined as the total number of **directly** connected roads to **either** city. If a road is directly connected to both cities, it is only counted **once**.

The **maximal network rank** of the infrastructure is the **maximum network rank** of all pairs of different cities.

Given the integer `n` and the array `roads`, return the ***maximal network rank** of the entire infrastructure*.


**Example 1:** 
![1615_ex1](./img/1615_ex1.png)
```
Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
```

**Example 2:** 
![1615_ex2](./img/1615_ex2.png)
```
Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.
```

**Example 3:** 
```
Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
```

Constraints:
    - `2 <= n <= 100` 
    - `0 <= roads.length <= n * (n - 1) / 2` 
    - `roads[i].length == 2` 
    - `0 <= ai, bi <= n-1` 
    - `ai != bi` 
    - Each pair of cities has **at most one** road connecting them.
"""

from typing import List
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Create graph
        graph = defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)

        max_rank = 0
        for u in range(n - 1):
            for v in range(u + 1, n):
                # Count the number of edges that are directly connected to u and v
                rank = len(graph[u]) + len(graph[v])
                # If u and v are directly connected, minus 1 since we are counting edge uv twice
                rank -= 1 if v in graph[u] else 0
                max_rank = max(max_rank, rank)
        return max_rank

# 4
print(Solution().maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))

# 5
print(Solution().maximalNetworkRank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))

# 5
print(Solution().maximalNetworkRank(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))

# 1
print(Solution().maximalNetworkRank(2, [[1, 0]]))

# 3
print(Solution().maximalNetworkRank(3, [[0, 1], [1, 2], [2, 0]]))

# 5
print(Solution().maximalNetworkRank(4, [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]]))

