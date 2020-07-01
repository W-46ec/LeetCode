
class Node:
	def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next

def initTree(l, idx, tree):
	if len(l) == 0:
		return Node(None)
	tree.val = l[idx]
	if 2 * idx + 1 < len(l) and l[2 * idx + 1] != None:
		tree.left = Node(None)
		initTree(l, 2 * idx + 1, tree.left)
	if 2 * idx + 2 < len(l) and l[2 * idx + 2] != None:
		tree.right = Node(None)
		initTree(l, 2 * idx + 2, tree.right)

def printSoln(root):
	while root:
		node = root
		while node:
			print(node.val, end = ' ')
			node = node.next
		print('#', end = ' ')
		root = root.left
	print()

class Solution:
	def connect(self, root: 'Node') -> 'Node':
		if root == None:
			return root
		count, level, Q = 0, 1, [root]
		while len(Q) > 0:
			node = Q.pop(0)
			count += 1
			if node.left != None:
				Q.append(node.left)
				Q.append(node.right)
			if count == (2 ** level - 1):
				level += 1
				node.next = None
			else:
				node.next = Q[0] if len(Q) else None
		return root

t1 = Node(None)
initTree([1, 2, 3], 0, t1)
t2 = Node(None)
initTree([1, 2, 3, 4, 5, 6, 7], 0, t2)

printSoln(Solution().connect(t1))
printSoln(Solution().connect(t2))

