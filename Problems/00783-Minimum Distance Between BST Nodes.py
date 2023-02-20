
"""
# Minimum Distance Between BST Nodes

Given the root of a Binary Search Tree (BST), return *the minimum difference between the values of any two different nodes in the tree*.


**Example 1:** 
![783_bst1](./img/783_bst1.jpg)
```
Input: root = [4,2,6,1,3]
Output: 1
```

**Example 2:** 
![783_bst2](./img/783_bst2.jpg)
```
Input: root = [1,0,48,null,null,12,49]
Output: 1
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[2, 100]`.
    - `0 <= Node.val <= 10^5` 

**Note**: This question is the same as 530: [https://leetcode.com/problems/minimum-absolute-difference-in-bst/](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path += ['.', '../', '../../']

from util import TreeNode, deserializeTree
from typing import Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff, prev = float('inf'), float('-inf')
        def inorder(tree):
            nonlocal min_diff, prev
            if not tree:
                return
            inorder(tree.left)
            min_diff, prev = min(min_diff, tree.val - prev), tree.val
            inorder(tree.right)
        inorder(root)
        return min_diff

# 1
print(Solution().getMinimumDifference(deserializeTree("[4, 2, 6, 1, 3]")))

# 1
print(Solution().getMinimumDifference(deserializeTree("[1, 0, 48, null, null, 12, 49]")))

# 1
print(Solution().getMinimumDifference(deserializeTree("[2, 1]")))
