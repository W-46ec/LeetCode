
"""
# All Nodes Distance K in Binary Tree

Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return *an array of the values of all nodes that have a distance `k` from the target node*.

You can return the answer in **any order**.


**Example 1:** 
![863_sketch0](./img/863_sketch0.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
```

**Example 2:** 
```
Input: root = [1], target = 1, k = 3
Output: []
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 500]`.
    - `0 <= Node.val <= 500` 
    - All the values `Node.val` are unique.
    - `target` is the value of one of the nodes in the tree.
    - `0 <= k <= 1000` 
"""

import sys
sys.path += ['.', '../', '../../']

from typing import List
from util import TreeNode, deserializeTree
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # The first BFS starts from the `root` node and
        # records the parent node of each node in the tree.
        parents = defaultdict(None) # Maps from nodes to parent nodes
        queue = [(root, None)]      # node, parent_node
        while queue:
            node, parent_node = queue.pop(0)
            parents[node] = parent_node
            queue += [(node.left, node)] if node.left else []
            queue += [(node.right, node)] if node.right else []

        # The second BFS starts from the `target` node and
        # obtains nodes with distance k from the `target`.
        ans = []
        queue = [(target, 0)]   # node, distance from target
        visited = defaultdict(bool, { target: True })
        while queue:
            node, dist = queue.pop(0)
            ans += [node.val] if dist == k else []
            for neighbor in [node.left, node.right, parents[node]]:
                if neighbor and not visited[neighbor] and dist < k:
                    queue += [(neighbor, dist + 1)]
                    visited[neighbor] = True

        return ans


# Utility function
def _search_node(tree: TreeNode, target_val: int) -> TreeNode:
    stack = [tree]
    while stack:
        node = stack.pop()
        if node.val == target_val:
            return node
        stack += [node.left] if node.left else []
        stack += [node.right] if node.right else []
    return None

# [7, 4, 1]
tree = deserializeTree("[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]")
print(Solution().distanceK(tree, _search_node(tree, 5), 2))

# []
tree = deserializeTree("[1]")
print(Solution().distanceK(tree, _search_node(tree, 1), 3))

# [2]
tree = deserializeTree("[0, 2, 1, null, null, 3]")
print(Solution().distanceK(tree, _search_node(tree, 3), 3))
