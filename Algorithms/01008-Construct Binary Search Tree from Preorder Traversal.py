
"""
# Construct Binary Search Tree from Preorder Traversal

Given an array of integers preorder, which represents the **preorder traversal** of a BST (i.e., **binary search tree**), construct the tree and return *its root*.

It is **guaranteed** that there is always possible to find a binary search tree with the given requirements for the given test cases.

A **binary search tree** is a binary tree where for every node, any descendant of `Node.left` has a value **strictly less than** `Node.val`, and any descendant of `Node.right` has a value **strictly greater than** `Node.val`.

A **preorder traversal** of a binary tree displays the value of the node first, then traverses `Node.left`, then traverses `Node.right`.


**Example 1:** 
![1008_1266](./img/1008_1266.png)
```
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
```

**Example 2:** 
```
Input: preorder = [1,3]
Output: [1,null,3]
```

**Constraints:** 
    - `1 <= preorder.length <= 100` 
    - `1 <= preorder[i] <= 10^8` 
    - All the values of preorder are **unique**.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from typing import List
from util import TreeNode, serializeTree

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def insert(tree, val):
            if tree == None:
                return TreeNode(val)
            if val <= tree.val:
                tree.left = insert(tree.left, val)
            else:
                tree.right = insert(tree.right, val)
            return tree
        root = None
        for i in preorder:
            root = insert(root, i)
        return root

# "[8, 5, 10, 1, 7, null, 12]"
print(serializeTree(Solution().bstFromPreorder(
    [8, 5, 1, 7, 10, 12]
)))

# "[1, null, 3]"
print(serializeTree(Solution().bstFromPreorder(
    [1, 3]
)))
