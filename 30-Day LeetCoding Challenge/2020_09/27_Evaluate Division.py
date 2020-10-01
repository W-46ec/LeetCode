
"""
# Evaluate Division

You are given `equations` in the format `A / B = k`, where `A` and `B` are variables represented as strings, and `k` is a real number (floating-point number). Given some `queries`, return the answers. If the answer does not exist, return `-1.0`.

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


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
    - `1 <= equations[i][0], equations[i][1] <= 5` 
    - `values.length == equations.length` 
    - `0.0 < values[i] <= 20.0` 
    - `1 <= queries.length <= 20` 
    - `queries[i].length == 2` 
    - `1 <= queries[i][0], queries[i][1] <= 5` 
    - `equations[i][0], equations[i][1], queries[i][0], queries[i][1]` consist of lower case English letters and digits.

**Hint #1** 
Do you recognize this as a graph problem?
"""

from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for idx, (x, y) in enumerate(equations):
            if x in graph:
                graph[x][y] = values[idx]
            else:
                graph[x] = { y: values[idx] }
            if y in graph:
                graph[y][x] = 1 / values[idx]
            else:
                graph[y] = { x: 1 / values[idx] }

        def graphSearch(graph, visited, x, y, coeff):
            if x not in graph or visited[x]:
                return -1.0
            if y in graph[x]:
                return coeff * graph[x][y]
            visited[x] = True
            for key in graph[x]:
                res = graphSearch(graph, visited, key, y, graph[x][key])
                if res != -1.0:
                    return coeff * res
            return -1.0

        return [graphSearch(graph, {k: False for k in graph}, x, y, 1.0) for x, y in queries]


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

