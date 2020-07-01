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
	def levelOrderTraverseTree(self, tree):
		l = []
		queue = []
		if tree != None:
			l.append(tree.val)
			queue.append(tree)
		while len(queue) != 0:
			t = queue.pop(0)
			if t.left != None:
				l.append(t.left.val)
				queue.append(t.left)
			else:
				l.append(None)
			if t.right != None:
				l.append(t.right.val)
				queue.append(t.right)
			else:
				l.append(None)
		return l

	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		l1 = self.levelOrderTraverseTree(p)
		l2 = self.levelOrderTraverseTree(q)
		if len(l1) == len(l2):
			for i in range(len(l1)):
				if l1[i] != l2[i]:
					return False
		else:
			return False
		return True

t1 = TreeNode(None)
initTree([1, 3], 0, t1)
t2 = TreeNode(None)
initTree([1, None, 3], 0, t2)
print(levelOrderTraverseTree(t1))
print(levelOrderTraverseTree(t2))

print(Solution().isSameTree(t1, t2))