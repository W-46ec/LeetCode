
"""
# Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

**Note:** 
You may assume that duplicates do not exist in the tree.

For example, given
```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Return the following binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```
"""

# Reference: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/758662/Python-O(n)-recursion-explained-with-diagram


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from util import TreeNode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_indices = {
            val: idx for idx, val in enumerate(inorder)
        }

        def traverse(post_beg, post_end, in_beg, in_end):
            if post_end <= post_beg:
                return None

            # Find the index of current root in inorder traversal list
            idx = inorder_indices[postorder[post_end - 1]]
            root = TreeNode(inorder[idx])

            # The portion of left subtree in the inorder list is given by [in_beg : idx]
            # The portion of right subtree in the inorder list is given by [idx + 1 : in_end]
            # The lengths of left and right are given by (idx - in_beg) and (in_end - idx)
            # Now we can obtain the portions of left and right subtree from the post order list:
            # Left subtree in the postorder list: [post_beg : idx]
            # Right subtree in the postorder list: [idx + 1 : in_end]

            # Construct both subtrees recursively
            root.left  = traverse(post_beg, post_beg + idx - in_beg, in_beg, idx)
            root.right = traverse(post_end - in_end + idx, post_end - 1, idx + 1, in_end)
            return root

        return traverse(0, len(postorder), 0, len(inorder))


