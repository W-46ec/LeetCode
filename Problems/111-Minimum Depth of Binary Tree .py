
"""
# Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.


**Example 1:** 
![22_ex_depth](./img/111_ex_depth.jpg)
```
Input: root = [3,9,20,null,null,15,7]
Output: 2
```

**Example 2:** 
```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[0, 10^5]`.
    - `-1000 <= Node.val <= 1000` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if not node.left and not node.right:
                return level
            queue += [(node.left, level + 1)] if node.left else []
            queue += [(node.right, level + 1)] if node.right else []

# 2
print(Solution().minDepth(deserializeTree("[3,9,20,null,null,15,7]")))

# 5
print(Solution().minDepth(deserializeTree("[2,null,3,null,4,null,5,null,6]")))

