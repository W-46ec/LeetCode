
"""
# Shortest Path Visiting All Nodes

You have an undirected, connected graph of `n` nodes labeled from `0` to `n - 1`. You are given an array `graph` where `graph[i]` is a list of all the nodes connected with node `i` by an edge.

Return *the length of the shortest path that visits every node*. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.


**Example 1:** 
![847_shortest1-graph](./img/847_shortest1-graph.jpg)
```
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
```

**Example 2:** 
![847_shortest2-graph](./img/847_shortest2-graph.jpg)
```
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
```

**Constraints:** 
    - `n == graph.length` 
    - `1 <= n <= 12` 
    - `0 <= graph[i].length < n` 
    - `graph[i]` does not contain `i`.
    - If `graph[a]` contains `b`, then `graph[b]` contains `a`.
    - The input graph is always connected.
"""

from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_visited = (1 << n) - 1
        queue = [(i, 0, 1 << i) for i in range(n)]
        seen = { (i, 1 << i) for i in range(n) }

        while queue:
            node, cost, path = queue.pop(0)
            if path == all_visited:
                return cost
            for neighbor in graph[node]:
                if (neighbor, path | (1 << neighbor)) not in seen:
                    queue += [(neighbor, cost + 1, path | (1 << neighbor))]
                    seen.add((neighbor, path | (1 << neighbor)))


# 4
print(Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]]))

# 4
print(Solution().shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))

# 14
print(Solution().shortestPathLength([[2, 3, 5, 7], [2, 3, 7], [0, 1], [0, 1], [7], [0], [10], [9, 10, 0, 1, 4], [9], [7, 8], [7, 6]]))

