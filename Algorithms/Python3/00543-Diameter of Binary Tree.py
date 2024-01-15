
"""
# Diameter of Binary Tree

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.


**Example 1:** 
![543_diamtree](./img/543_diamtree.jpg)
```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:** 
```
Input: root = [1,2]
Output: 1
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-100 <= Node.val <= 100` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import sys
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def solve(tree):
            if tree == None:
                return [-1, -1]
            if tree.left == None and tree.right == None:
                return [0, 0]
            lheight, ldiameter = solve(tree.left)
            rheight, rdiameter = solve(tree.right)
            diameter = max(ldiameter, rdiameter, lheight + rheight + 2)
            return [max(lheight + 1, rheight + 1), diameter]
        ans = solve(root)[1]
        return ans if ans >= 0 else 0

# 3
print(Solution().diameterOfBinaryTree(deserializeTree(
    "[1, 2, 3, 4, 5]"
)))

# 1
print(Solution().diameterOfBinaryTree(deserializeTree(
    "[1, 2]"
)))

# 8
print(Solution().diameterOfBinaryTree(deserializeTree(
    "[4, -7, -3, null, null, -9, -3, 9, -7, -4, null, 6, null, -6, -6, null, null, 0, 6, 5, null, 9, null, null, -1, -4, null, null, null, -2]"
)))
