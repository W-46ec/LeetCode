
"""
# Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
    1. Search for a node to remove.
    2. If the node is found, delete the node.

**Note:** Time complexity should be O(height of tree).

**Example:** 
```
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
```
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, initTree

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        node, parent, childNum = root, None, None
        while node.val != key:
            if key < node.val and node.left:
                node, parent, childNum = node.left, node, 0
                continue
            elif key > node.val and node.right:
                node, parent, childNum = node.right, node, 1
                continue
            return root

        if not node.left and not node.right:
            if not parent:
                return None
            if childNum == 0:
                parent.left = None
            else:
                parent.right = None
        elif not node.right:
            if not parent:
                return node.left
            if childNum == 0:
                parent.left = node.left
            else:
                parent.right = node.left
        elif not node.left:
            if not parent:
                return node.right
            if childNum == 0:
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            # Find successor
            succ = node.right
            while succ and succ.left:
                succ = succ.left
            node.val = succ.val
            node.right = self.deleteNode(node.right, succ.val)
        return root


