
"""
# Find Nearest Right Node in Binary Tree

Given the `root` of a binary tree and a node `u` in the tree, return *the **nearest** node on the **same level** that is to the **right** of `u`, or return `null` if `u` is the rightmost node in its level*.


**Example 1:** 
![1602_p3](./img/1602_p3.png)
```
Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.
```

**Example 2:** 
![1602_p2](./img/1602_p2.png)
```
Input: root = [3,null,4,2], u = 2
Output: null
Explanation: There are no nodes to the right of 2.
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^5]`.
    - `1 <= Node.val <= 10^5` 
    - All values in the tree are **distinct**.
    - `u` is a node in the binary tree rooted at `root`.
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
from util import TreeNode, serializeTree, deserializeTree

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        queue = [(0, root)]
        for level, node in queue:
            queue += [(level + 1, node.left)] if node.left else []
            queue += [(level + 1, node.right)] if node.right else []
        for idx, (level, node) in enumerate(queue):
            if node.val == u.val:
                if idx + 1 < len(queue) and level == queue[idx + 1][0]:
                    return queue[idx + 1][1]
                else:
                    return None

# [5]
print(serializeTree(Solution().findNearestRightNode(
    deserializeTree("[1, 2, 3, null, 4, 5, 6]"), 
    deserializeTree("[4]")
)))

# []
print(serializeTree(Solution().findNearestRightNode(
    deserializeTree("[3, null, 4, 2]"), 
    deserializeTree("[2]")
)))
