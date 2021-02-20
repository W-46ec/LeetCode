
"""
# Trim a Binary Search Tree

Given the `root` of a binary search tree and the lowest and highest boundaries as `low` and `high`, trim the tree so that all its elements lies in `[low, high]`. Trimming the tree should **not** change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a **unique answer**.

Return *the root of the trimmed binary search tree*. Note that the root may change depending on the given bounds.


**Example 1:** 
![669_trim1](./img/669_trim1.jpg)
```
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
```

**Example 2:** 
![669_trim2](./img/669_trim2.jpg)
```
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
```

**Example 3:** 
```
Input: root = [1], low = 1, high = 2
Output: [1]
```

**Example 4:** 
```
Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]
```

**Example 5:** 
```
Input: root = [1,null,2], low = 2, high = 4
Output: [2]
```

**Constraints:** 
    - The number of nodes in the tree in the range `[1, 10^4]`.
    - `0 <= Node.val <= 10^4` 
    - The value of each node in the tree is **unique**.
    - `root` is guaranteed to be a valid binary search tree.
    - `0 <= low <= high <= 10^4` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, serializeTree, deserializeTree

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root:
            if root.val < low:
                root = self.trimBST(root.right, low, high)
            elif root.val > high:
                root = self.trimBST(root.left, low, high)
            else:
                root.left = self.trimBST(root.left, low, high)
                root.right = self.trimBST(root.right, low, high)
        return root

# [1, null, 2]
print(serializeTree(Solution().trimBST(deserializeTree("[1, 0, 2]"), 1, 2)))

# [3, 2, null, 1]
print(serializeTree(Solution().trimBST(deserializeTree("[3, 0, 4, null, 2, null, null, 1]"), 1, 3)))

# [1]
print(serializeTree(Solution().trimBST(deserializeTree("[1]"), 1, 2)))

# [1, null, 2]
print(serializeTree(Solution().trimBST(deserializeTree("[1, null, 2]"), 1, 3)))

# [2]
print(serializeTree(Solution().trimBST(deserializeTree("[1, null, 2]"), 2, 4)))

# []
print(serializeTree(Solution().trimBST(deserializeTree("[1, null, 2]"), 4, 5)))

