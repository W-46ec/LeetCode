
"""
# All Paths From Source to Target

Given a directed, acyclic graph of `N` nodes. Find all possible paths from node `0` to node `N-1`, and return them in any order.

The graph is given as follows: the nodes are 0, 1, ..., graph.length - 1. graph[i] is a list of all nodes j for which the edge (i, j) exists.

```
Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

**Note:** 
    - The number of nodes in the graph will be in the range `[2, 15]`.
    - You can print different paths in any order, but you should keep the order of nodes inside one path.
"""

from typing import List
from collections import defaultdict

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Build a directed graph
        N, g = len(graph), defaultdict(list)
        for i in range(N):
            g[i] += graph[i]

        # Run DFS to find all the paths from node 0 to node N - 1
        ans, stack = [], [(0, [0])]
        while stack:
            node, path = stack.pop()
            ans += [path] if node == N - 1 else []
            stack += [(dst, path + [dst]) for dst in g[node]]
        return ans

print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))  # [[0, 2, 3], [0, 1, 3]]

