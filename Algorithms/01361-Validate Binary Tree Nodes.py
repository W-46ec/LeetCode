
"""
# Validate Binary Tree Nodes

You have `n` binary tree nodes numbered from `0` to `n - 1` where node `i` has two children `leftChild[i]` and `rightChild[i]`, return `true` if and only if **all** the given nodes form **exactly one** valid binary tree.

If node `i` has no left child then `leftChild[i]` will equal `-1`, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.


**Example 1:** 
![1361_1503_ex1](./img/1361_1503_ex1.png)
```
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
```

**Example 2:** 
![1361_1503_ex2](./img/1361_1503_ex2.png)
```
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
```

**Example 3:** 
![1361_1503_ex3](./img/1361_1503_ex3.png)
```
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
```

**Constraints:** 
    - `n == leftChild.length == rightChild.length` 
    - `1 <= n <= 10^4` 
    - `-1 <= leftChild[i], rightChild[i] <= n - 1` 
"""

from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Find the root node -- root node has no incoming edges
        nodes = set(range(n))
        for i in range(n):
            for lst in [leftChild, rightChild]:
                if lst[i] != -1:
                    nodes.discard(lst[i])
        # A valid binary tree should have exactly one root
        if len(nodes) != 1:
            return False

        # Run BFS to traverse the tree
        root, visited = list(nodes)[0], [False] * n
        queue, visited[root] = [root], True
        while queue:
            node = queue.pop(0)
            for lst in [leftChild, rightChild]:
                if lst[node] != -1:
                    # If the child node has been visited, return False
                    if visited[lst[node]]:
                        return False
                    queue += [lst[node]]
                    visited[lst[node]] = True

        # All nodes should be visited
        return all(visited)

# True
print(Solution().validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]))

# False
print(Solution().validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, 3, -1, -1]))

# False
print(Solution().validateBinaryTreeNodes(2, [1, 0], [-1, -1]))

# True
print(Solution().validateBinaryTreeNodes(2, [1, -1], [-1, -1]))

# False
print(Solution().validateBinaryTreeNodes(4, [1, 0, 3, -1], [-1, -1, -1, -1]))