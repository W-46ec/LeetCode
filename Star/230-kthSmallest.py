

def inorder(tree):
    def _inorder(node):
        if node.left:
            for other in _inorder(node.left):
                yield other
        yield node
        if node.right:
            for other in _inorder(node.right):
                yield other
    
    for node in _inorder(tree):
        yield node

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        i = 0
        for node in inorder(root):
            i += 1
            if i == k:
                return node.val