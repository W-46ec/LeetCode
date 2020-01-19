
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        def traverse(root):
            if root == None:
                return
            ans.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root1)
        traverse(root2)
        return sorted(ans)