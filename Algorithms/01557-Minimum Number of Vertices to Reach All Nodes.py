
"""
# Minimum Number of Vertices to Reach All Nodes

Given a **directed acyclic graph**, with `n` vertices numbered from `0` to `n-1`, and an array `edges` where `edges[i] = [from_i, to_i]` represents a directed edge from node `from_i` to node `to_i`.

Find *the smallest set of vertices from which all nodes in the graph are reachable*. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.


**Example 1:** 
![1557_untitled22](./img/1557_untitled22.png)
```
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
```

**Example 2:** 
![1557_untitled](./img/1557_untitled.png)
```
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
```

**Constraints:** 
    - `2 <= n <= 10^5` 
    - `1 <= edges.length <= min(10^5, n * (n - 1) / 2)` 
    - `edges[i].length == 2` 
    - `0 <= from_i, to_i < n` 
    - All pairs `(from_i, to_i)` are distinct.
"""

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Set cover problem for DAG
        # Return the set of vertices with in-degree equal to 0
        # Explanation:
        #     Any vertex v with in-degree 0 must be in the solution set.
        #     Otherwise, there is no way we can reach v from other nodes.
        #     Since unique solution is guaranteed, nodes with in-degree > 0 must
        #     be reachable from at least one of the nodes with in-degree 0.
        #     Therefore, nodes with in-degree 0 form the minimal solution set.

        # # Iteration
        # in_degree = [0] * n
        # for u, v in edges:
        #     in_degree[v] += 1
        # return [i for i in range(len(in_degree)) if in_degree[i] == 0]

        # Set
        return set(range(n)) - set([v for _, v in edges])

# [0, 3]
print(Solution().findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))

# [0, 2, 3]
print(Solution().findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
