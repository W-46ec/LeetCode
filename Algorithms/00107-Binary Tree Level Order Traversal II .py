
"""
# Binary Tree Level Order Traversal II

Given a binary tree, return the *bottom-up level order* traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```

return its bottom-up level order traversal as:
```
[
  [15,7],
  [9,20],
  [3]
]
```
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        Q = [(root, 0)]
        while Q:
            node, level = Q.pop(0)
            if level < len(ans):
                ans[len(ans) - level - 1].append(node.val)
            else:
                ans = [[node.val]] + ans
            if node.left != None:
                Q.append((node.left, level + 1))
            if node.right != None:
                Q.append((node.right, level + 1))
        return ans



