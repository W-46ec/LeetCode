
"""
# Evaluate Division

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the `jth` query where you must find the answer for `Cj / Dj = ?`.

Return *the answers to all queries*. If a single answer cannot be determined, return `-1.0`.

**Note**: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.


**Example 1:** 
```
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
```

**Example 2:** 
```
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
```

**Example 3:** 
```
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
```

**Constraints:** 
    - `1 <= equations.length <= 20` 
    - `equations[i].length == 2` 
    - `1 <= Ai.length, Bi.length <= 5` 
    - `values.length == equations.length` 
    - `0.0 < values[i] <= 20.0` 
    - `1 <= queries.length <= 20` 
    - `queries[i].length == 2` 
    - `1 <= Cj.length, Dj.length <= 5` 
    - `Ai, Bi, Cj, Dj` consist of lower case English letters and digits.
"""

from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Use an undirected weighted graph to represent the equations
        # (i.e., graph[u] <- list of nodes that are adjacent of u)
        graph = defaultdict(list)
        for idx, (x, y) in enumerate(equations):
            graph[x] += [(y, values[idx])]
            graph[y] += [(x, 1 / values[idx])]

        # Run BFS to find the answer for each query.
        # For any query [x, y], if x, y are in the same connected component in the graph, 
        # the answer can be determined. Otherwise, there is no answer.
        ans = [-1.0] * len(queries)
        for idx, (src, dst) in enumerate(queries):
            # Make sure the variable exists in the graph
            if src in graph:
                # BFS
                queue, visited = [(src, 1)], { k: False for k in graph }
                visited[src] = True
                while queue:
                    node, cumm_weight = queue.pop(0)
                    if node == dst:
                        ans[idx] = cumm_weight
                        break
                    for neighbor, weight in graph[node]:
                        if not visited[neighbor]:
                            queue += [(neighbor, cumm_weight * weight)]
                            visited[neighbor] = True

        return ans


# [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
print(Solution().calcEquation(
    equations = [["a", "b"], ["b", "c"]], 
    values = [2.0, 3.0], 
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
))

# [3.75000, 0.40000, 5.00000, 0.20000]
print(Solution().calcEquation(
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]], 
    values = [1.5, 2.5, 5.0], 
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
))

# [0.50000, 2.00000, -1.00000, -1.00000]
print(Solution().calcEquation(
    equations = [["a", "b"]], 
    values = [0.5], 
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
))

# [360.00000, 0.00833, 20.00000, 1.00000, -1.00000, -1.00000]
print(Solution().calcEquation(
    equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]], 
    values = [3.0, 4.0, 5.0, 6.0], 
    queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
))

