# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def initTree(l, idx, tree):
	if len(l) == 0:
		return TreeNode(None)
	tree.val = l[idx]
	if 2 * idx + 1 < len(l) and l[2 * idx + 1] != None:
		tree.left = TreeNode(None)
		initTree(l, 2 * idx + 1, tree.left)
	if 2 * idx + 2 < len(l) and l[2 * idx + 2] != None:
		tree.right = TreeNode(None)
		initTree(l, 2 * idx + 2, tree.right)

def levelOrderTraverseTree(tree):
	l = []
	queue = []
	if tree != None:
		# print(tree.val, end = "")
		l.append(tree.val)
		queue.append(tree)
	while len(queue) != 0:
		t = queue.pop(0)
		if t.left != None:
			# print(t.left.val, end = "")
			l.append(t.left.val)
			queue.append(t.left)
		else:
			l.append(None)
		if t.right != None:
			# print(t.right.val, end = "")
			l.append(t.right.val)
			queue.append(t.right)
		else:
			l.append(None)
	return l

class Solution:
	def rangeSumBST(self, root, L, R):
		"""
		:type root: TreeNode
		:type L: int
		:type R: int
		:rtype: int
		"""
		def traverse(root):
			s = 0
			if root != None:
				if root.val >= L and root.val <= R:
					s += root.val
					s += traverse(root.left)
					s += traverse(root.right)
				elif root.val < L:
					s += traverse(root.right)
				else:
					s += traverse(root.left)
			return s
		return traverse(root)
		
t1 = TreeNode(None)
initTree([10, 5, 15, 3, 7, None, 18], 0, t1)
print(levelOrderTraverseTree(t1))
print(Solution().rangeSumBST(t1, 7, 15))