
"""
# Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

