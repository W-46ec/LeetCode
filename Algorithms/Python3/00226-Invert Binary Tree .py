
"""
# Invert Binary Tree

Given the `root` of a binary tree, invert the tree, and return *its root*.


**Example 1:** 
![226_invert1-tree](./img/226_invert1-tree.jpg)
```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2:** 
![226_invert2-tree](./img/226_invert2-tree.jpg)
```
Input: root = [2,1,3]
Output: [2,3,1]
```

**Example 3:** 
```
Input: root = []
Output: []
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100` 

**Trivia:** 
This problem was inspired by this original tweet by Max Howell:

> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, serializeTree, deserializeTree

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # def solve(tree):
        #     if tree == None:
        #         return
        #     tree.left, tree.right = tree.right, tree.left
        #     solve(tree.left)
        #     solve(tree.right)
        # solve(root)
        # return root
        
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# "[4, 7, 2, 9, 6, 3, 1]"
print(serializeTree(Solution().invertTree(deserializeTree(
    "[4, 2, 7, 1, 3, 6, 9]"
))))

# "[2, 3, 1]"
print(serializeTree(Solution().invertTree(deserializeTree(
    "[2, 1, 3]"
))))

# "[]"
print(serializeTree(Solution().invertTree(deserializeTree(
    "[]"
))))
