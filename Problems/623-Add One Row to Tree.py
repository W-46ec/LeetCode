
"""
# Add One Row to Tree

Given the `root` of a binary tree and two integers `val` and `depth`, add a row of nodes with value `val` at the given depth `depth`.

Note that the `root` node is at depth `1`.

The adding rule is:
    - Given the integer `depth`, for each not null tree node `cur` at the `depth depth - 1`, create two tree nodes with value `val` as `cur`'s left subtree root and right subtree root.
    - `cur`'s original left subtree should be the left subtree of the new left subtree root.
    - `cur`'s original right subtree should be the right subtree of the new right subtree root.
    - If `depth == 1` that means there is no depth `depth - 1` at all, then create a tree node with value `val` as the new root of the whole original tree, and the original tree is the new root's left subtree.

**Example 1:** 
![623_addrow-tree](./img/623_addrow-tree.jpg)
```
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]
```

**Example 2:** 
![623_add2-tree](./img/623_add2-tree.jpg)
```
Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - The depth of the tree is in the range `[1, 10^4]`.
    - `-100 <= Node.val <= 100` 
    - ` -10^5 <= val <= 10^5` 
    - `1 <= depth <= the depth of tree + 1` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree, serializeTree

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        dummy = TreeNode(0, root)
        row = [dummy]
        for _ in range(depth - 1):
            row = [child for node in row for child in [node.left, node.right] if child]
        for node in row:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return dummy.left

# [4, 1, 1, 2, null, null, 6, 3, 1, 5]
print(serializeTree(Solution().addOneRow(deserializeTree("[4, 2, 6, 3, 1, 5]"), 1, 2)))

# [4, 2, null, 1, 1, 3, null, null, 1]
print(serializeTree(Solution().addOneRow(deserializeTree("[4, 2, null, 3, 1]"), 1, 3)))

