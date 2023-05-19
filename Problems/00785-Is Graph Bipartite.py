
"""
# Is Graph Bipartite

There is an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. More formally, for each `v` in `graph[u]`, there is an undirected edge between node `u` and node `v`. The graph has the following properties:

    - There are no self-edges (`graph[u]` does not contain `u`).
    - There are no parallel edges (`graph[u]` does not contain duplicate values).
    - If `v` is in `graph[u]`, then `u` is in `graph[v]` (the graph is undirected).
    - The graph may not be connected, meaning there may be two nodes `u` and `v` such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return `true` *if and only if it is **bipartite***.


**Example 1:** 
![785_bi2](./img/785_bi2.jpg)
```
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
```

**Example 2:** 
![785_bi1](./img/785_bi1.jpg)
```
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
```

**Constraints:** 
    - `graph.length == n` 
    - `1 <= n <= 100` 
    - `0 <= graph[u].length < n` 
    - `0 <= graph[u][i] <= n - 1` 
    - `graph[u]` does not contain `u`.
    - All the values of `graph[u]` are **unique**.
    - If `graph[u]` contains `v`, then `graph[v]` contains `u`.
"""

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Run BFS to color the graph - O(n) time
        # The graph is bipartite only if the graph is 2-colorable
        # The color value (i.e., `curr_color`) is either 0 or 1
        # Start with any node and assign color 0 to that node.
        # In each iteration, we assign the alternate color to the neighbor nodes.
        # If any two adjacent nodes are assigned the same color, 
        # the graph is not 2-colorable and therefore not bipartite. Return False.
        # If we can constitently color all nodes in the graph, 
        # the graph is 2-colorable and hence bipartite. Return True.

        # colors[i]:
        #     -1: not visited
        #      0: color 0 is assigned to node i
        #      1: color 1 is assigned to node i
        queue, colors = [], [-1] * len(graph)
        for node in range(len(graph)):
            # Node is not yet visited
            if colors[node] == -1:
                # Add node to queue
                queue += [node]
                # Assign color 0 to the node
                colors[node] = 0
                # Run BFS for the connected component
                while queue:
                    src_node = queue.pop(0)
                    curr_color = colors[src_node]
                    for dst_node in graph[src_node]:
                        # If neighbor node is not visited, 
                        # assign alternate color and add node to queue
                        if colors[dst_node] == -1:
                            colors[dst_node] = (curr_color + 1) % 2
                            queue += [dst_node]
                        # If neighbor node is visited, 
                        # check whether or not the assigned color is consistent
                        elif colors[dst_node] != (curr_color + 1) % 2:
                            return False
        return True

# False
print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))

# True
print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))

# False
print(Solution().isBipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]))
