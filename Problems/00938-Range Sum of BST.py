
"""
# Range Sum of BST

Given the `root` node of a binary search tree, return *the sum of values of all nodes with a value in the range `[low, high]`*.


**Example 1:** 
![938_bst1](./img/938_bst1.jpg)
```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
```

**Example 2:** 
![938_bst2](./img/938_bst2.jpg)
```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
```

**Constraints:** 
    - `The number of nodes in the tree is in the range `[1, 2 * 10^4]`.
    - `1 <= Node.val <= 10^5` 
    - `1 <= low <= high <= 10^5` 
    - All `Node.val` are **unique**.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        else:
            return self.rangeSumBST(root.left, low, high)

# 32
print(Solution().rangeSumBST(deserializeTree("[10, 5, 15, 3, 7, null, 18]"), 7, 15))

# 23
print(Solution().rangeSumBST(deserializeTree("[10, 5, 15, 3, 7, 13, 18, 1, null, 6]"), 6, 10))

