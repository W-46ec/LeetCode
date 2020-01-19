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
	def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
		locations = []
		def traverse(r, parentVal, depth):
			if r == None:
				return
			if r.val == x:
				locations.append((x, parentVal, depth))
			if r.val == y:
				locations.append((y, parentVal, depth))
			traverse(r.left, r.val, depth + 1)
			traverse(r.right, r.val, depth + 1)

		traverse(root, None, 0)
		# print(locations)
		if len(locations) < 2:
			return False
		if locations[0][1] == locations[1][1]:
			return False
		if locations[0][2] != locations[1][2]:
			return False
		return True

t1 = TreeNode(None)
initTree([1, 2, 3, None, 4, None, 5], 0, t1)
t2 = TreeNode(None)
initTree([1, 2, 3, None, 4], 0, t2)
print(levelOrderTraverseTree(t1))
print(levelOrderTraverseTree(t2))

print(Solution().isCousins(t1, 4, 5))
print(Solution().isCousins(t2, 2, 3))