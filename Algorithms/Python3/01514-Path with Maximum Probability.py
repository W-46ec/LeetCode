
"""
# Path with Maximum Probability

You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a, b]` is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing that edge `succProb[i]`.

Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability.

If there is no path from `start` to `end`, **return 0**. Your answer will be accepted if it differs from the correct answer by at most **1e-5**.


**Example 1:** 
![1514_1558_ex1](./img/1514_1558_ex1.png)
```
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
```

**Example 2:** 
![1514_1558_ex2](./img/1514_1558_ex2.png)
```
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
```

**Example 3:** 
![1514_1558_ex3](./img/1514_1558_ex3.png)
```
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
```

**Constraints:** 
    - `2 <= n <= 10^4` 
    - `0 <= start, end < n` 
    - `start != end` 
    - `0 <= a, b < n` 
    - `a != b` 
    - `0 <= succProb.length == edges.length <= 2*10^4` 
    - `0 <= succProb[i] <= 1` 
    - There is at most one edge between every two nodes.
"""

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Create graph
        graph = defaultdict(list)
        for idx, (u, v) in enumerate(edges):
            graph[u] += [(v, succProb[idx])]
            graph[v] += [(u, succProb[idx])]

        # Run Dijkstra's algorithm
        heap = [(-1.0, start)]  # -probability, node (use negative prob so we can use the built-in min heap)
        max_prob = [0] * n      # max probability for each node
        max_prob[start] = 1.0   # max probability for start node is 1
        while heap:
            # Pop the node in the fringe with max prob (or min negative prob)
            neg_prob, node = heapq.heappop(heap)
            # Explore its neighbors
            for neighbor, edge_prob in graph[node]:
                # Update max prob for neighbor if we find a better path
                if -neg_prob * edge_prob > max_prob[neighbor]:
                    max_prob[neighbor] = -neg_prob * edge_prob
                    heapq.heappush(heap, (neg_prob * edge_prob, neighbor))

        # Return max prob for the end node
        return max_prob[end]

# 0.25
print(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))

# 0.3
print(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))

# 0
print(Solution().maxProbability(3, [[0, 1]], [0.5], 0, 2))
