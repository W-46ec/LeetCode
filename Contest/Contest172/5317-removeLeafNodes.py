
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
	def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
		empty = False
		def solve(tree, parent, child):
			if tree == None:
				return
			if tree.left != None:
				solve(tree.left, tree, 0)
			if tree.right != None:
				solve(tree.right, tree, 1)
			if tree.left == None and tree.right == None and tree.val == target:
				if child == -1:
					return True
				elif child == 0:
					parent.left = None
				else:
					parent.right = None
		empty = solve(root, None, -1)
		return root if not empty else None

root1 = TreeNode(None)
initTree([1, 2, 3, 2, None, 2, 4], 0, root1)
root2 = TreeNode(None)
initTree([1, 3, 3, 3, 2], 0, root2)
root3 = TreeNode(None)
initTree([1, 2, None, 2, None, 2], 0, root3)
root4 = TreeNode(None)
initTree([1, 1, 1], 0, root4)

print(levelOrderTraverseTree(Solution().removeLeafNodes(root1, target = 2)))
print(levelOrderTraverseTree(Solution().removeLeafNodes(root2, target = 3)))
print(levelOrderTraverseTree(Solution().removeLeafNodes(root3, target = 2)))
print(levelOrderTraverseTree(Solution().removeLeafNodes(root4, target = 1)))
