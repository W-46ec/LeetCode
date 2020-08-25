
"""
# Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

**Example:** 
```
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
```
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path.append('../../')

from util import TreeNode, initTree

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        Q, left_leaves = [(root, False)], []
        while Q:
            node, isLeft = Q.pop(0)
            left_leaves += [node.val] if not node.left and not node.right and isLeft else []
            Q += [(node.left, True)] if node.left else []
            Q += [(node.right, False)] if node.right else []
        return sum(left_leaves)

print(Solution().sumOfLeftLeaves(initTree([3, 9, 20, None, None, 15, 7])))    # 24
print(Solution().sumOfLeftLeaves(initTree([3])))    # 0
