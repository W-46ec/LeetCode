
"""
# Binary Tree Maximum Path Sum

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one** node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Reference: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # self.ans = float('-inf')
        # def solve(tree):
        #     if tree == None:
        #         return 0
        #     # If the optimal value of left / right branch is negative, then we can
        #     # simply get a better value (0) by not selecting it.
        #     optLeft, optRight = max(solve(tree.left), 0), max(solve(tree.right), 0)
        #     optCurr = optLeft + optRight + tree.val
        #     self.ans = max(self.ans, optCurr)
        #     return max(optLeft + tree.val, optRight + tree.val)
        # solve(root)
        # return self.ans
        
        # ans = float('-inf')
        # def solve(tree):
        #     nonlocal ans
        #     if tree == None:
        #         return 0
        #     # If the optimal value of left / right branch is negative, then we can
        #     # simply get a better value (0) by not selecting it.
        #     optLeft, optRight = max(solve(tree.left), 0), max(solve(tree.right), 0)
        #     optCurr = optLeft + optRight + tree.val
        #     ans = max(ans, optCurr)
        #     return max(optLeft + tree.val, optRight + tree.val)
        # solve(root)
        # return ans
        
        ans = [float('-inf')]
        def solve(tree, ans):
            if tree == None:
                return 0
            # If the optimal value of left / right branch is negative, then we can
            # simply get a better value (0) by not selecting it.
            optLeft, optRight = max(solve(tree.left, ans), 0), max(solve(tree.right, ans), 0)
            optCurr = optLeft + optRight + tree.val
            ans[0] = max(ans[0], optCurr)
            return max(optLeft + tree.val, optRight + tree.val)
        solve(root, ans)
        return ans[0]


