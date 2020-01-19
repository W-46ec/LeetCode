
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		ele = []
		def traverse(tree):
			if not tree:
				return
			ele.append(tree.val)
			traverse(tree.left)
			traverse(tree.right)
		traverse(root)
		ele = sorted(ele)
		# print(ele)
		return ele[k - 1]

