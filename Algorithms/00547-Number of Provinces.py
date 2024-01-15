
"""
# Number of Provinces

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return *the total number of **provinces***.


**Example 1:** 
![547_graph1](./img/547_graph1.jpg)
```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Example 2:** 
![547_graph2](./img/547_graph2.jpg)
```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

**Constraints:** 
    - `1 <= n <= 200` 
    - `n == isConnected.length` 
    - `n == isConnected[i].length` 
    - `isConnected[i][j]` is `1` or `0`.
    - `isConnected[i][i] == 1` 
    - `isConnected[i][j] == isConnected[j][i]` 
"""

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, num_component = len(isConnected), 0
        visited = [False] * n
        # Check for un-visited nodes
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                num_component += 1
                # Run BFS to explore the connected component
                queue = [i]
                while queue:
                    node = queue.pop(0)
                    for neighbor, connected in enumerate(isConnected[node]):
                        if not visited[neighbor] and connected == 1:
                            queue += [neighbor]
                            visited[neighbor] = True
        return num_component

# 2
print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# 3
print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
