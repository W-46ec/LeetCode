
"""
# Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `n` nodes labelled from `0` to `n - 1`, and an array of `n - 1` `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between the two nodes `ai` and `bi` in the tree, you can choose any node of the tree as the root. When you select a node `x` as the root, the result tree has height `h`. Among all possible rooted trees, those with minimum height (i.e. `min(h)`) are called **minimum height trees** (MHTs).

Return *a list of all **MHTs'** root labels*. You can return the answer in **any order**.

The **height** of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


**Example 1:** 
![310_e1](./img/310_e1.jpg)
```
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
```

**Example 2:** 
![310_e2](./img/310_e2.jpg)
```
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
```

**Example 3:** 
```
Input: n = 1, edges = []
Output: [0]
```

**Example 4:** 
```
Input: n = 2, edges = [[0,1]]
Output: [0,1]
```

**Constraints:** 
    - `1 <= n <= 2 * 10^4` 
    - `edges.length == n - 1` 
    - `0 <= ai, bi < n` 
    - `ai != bi` 
    - All the pairs `(ai, bi)` are distinct.
    - The given input is **guaranteed** to be a tree and there will be **no repeated** edges.

**Hint #1** 
How many MHTs can a graph have at most?
"""

# Reference: https://leetcode.com/problems/minimum-height-trees/solution/

from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Construct the graph
        graph = defaultdict(set)
        for src, dst in edges:
            graph[src].add(dst)
            graph[dst].add(src)

        # Set of all nodes
        nodes = { i for i in range(n) }

        # Set of leaves of the current tree
        leaves = set(filter(lambda x: len(graph[x]) == 1, graph))

        # Keep trimming the leaves until the order of graph is <= 2
        while len(nodes) > 2:
            # Remove the set of leaves from the set of remaining nodes
            nodes -= leaves

            new_leaves = set()
            # Update the graph accordingly
            for leaf in leaves:
                for neighbor in graph.pop(leaf):
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        new_leaves.add(neighbor)

            # Set of leaves of the new tree
            leaves = new_leaves

        # Return the remaining nodes -- the centroids
        return list(nodes)


# [1]
print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))

# [3, 4]
print(Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))

# [0]
print(Solution().findMinHeightTrees(1, []))

# [0, 1]
print(Solution().findMinHeightTrees(2, [[0, 1]]))

