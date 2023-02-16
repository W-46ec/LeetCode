
"""
# Maximum Depth of Binary Tree

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.


**Example 1:** 
![104_tmp-tree](./img/104_tmp-tree.jpg)
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:** 
```
Input: root = [1,null,2]
Output: 2
```

**Example 3:** 
```
Input: root = []
Output: 0
```

**Example 4:** 
```
Input: root = [0]
Output: 1
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `-100 <= Node.val <= 100` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path += ['.', '../', '../../']

from typing import Optional
from util import TreeNode, deserializeTree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # Recursive approach
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Non-recursive approach -- DFS
        max_depth = 0
        stack = [(root, 1)] if root else []
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            stack += [(node.left, depth + 1)] if node.left else []
            stack += [(node.right, depth + 1)] if node.right else []
        return max_depth


# 3
print(Solution().maxDepth(deserializeTree("[3, 9, 20, null, null, 15, 7]")))

# 2
print(Solution().maxDepth(deserializeTree("[1, null, 2]")))

# 0
print(Solution().maxDepth(deserializeTree("[]")))

# 1
print(Solution().maxDepth(deserializeTree("[0]")))

