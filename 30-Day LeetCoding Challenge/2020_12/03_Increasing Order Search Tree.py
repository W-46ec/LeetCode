
"""
# Increasing Order Search Tree

Given the `root` of a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

**Example 1:** 
![03_ex1](./img/03_ex1.jpg)
```
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
```

**Example 2:** 
![03_ex2](./img/03_ex2.jpg)
```
Input: root = [5,1,7]
Output: [1,null,5,null,7]
```

**Constraints:** 
    - The number of nodes in the given tree will be in the range `[1, 100]`.
    - `0 <= Node.val <= 1000` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree, serializeTree

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans, curr = None, None
        def traverse(tree):
            nonlocal ans, curr
            if not tree:
                return
            traverse(tree.left)
            if ans:
                curr.right = TreeNode(tree.val)
                curr = curr.right
            else:
                ans = curr = TreeNode(tree.val)
            traverse(tree.right)
        traverse(root)
        return ans

# [1, null, 2, null, 3, null, 4, null, 5, null, 6, null, 7, null, 8, null, 9]
print(serializeTree(Solution().increasingBST(deserializeTree("[5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]"))))

# [1, null, 5, null, 7]
print(serializeTree(Solution().increasingBST(deserializeTree("[5, 1, 7]"))))

