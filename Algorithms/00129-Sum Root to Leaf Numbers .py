
"""
# Sum Root to Leaf Numbers

Given a binary tree containing digits from `0-9` only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path `1->2->3` which represents the number `123`.

Find the total sum of all root-to-leaf numbers.

**Note:** A leaf is a node with no children.

**Example:** 
```
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

**Example 2:** 
```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# from functools import reduce

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # # Recursive + Two-stack method
        # ans, num_stack = 0, []
        # def traverse(tree):
        #     nonlocal ans, num_stack
        #     if not tree:
        #         return
        #     num_stack.append(tree.val)
        #     if tree.left == None and tree.right == None:
        #         ans += reduce(lambda x, y: 10 * x + y, num_stack)
        #     if tree.left:
        #         traverse(tree.left)
        #     if tree.right:
        #         traverse(tree.right)
        #     num_stack.pop()
        # traverse(root)
        # return ans

        # # Recursive method
        # def traverse(tree, pathNum = 0):
        #     if not tree:
        #         return 0
        #     pathNum += tree.val
        #     if tree.left == None and tree.right == None:
        #         return pathNum
        #     return traverse(tree.left, pathNum * 10) + traverse(tree.right, pathNum * 10)
        # return traverse(root)

        # None-recursive method
        if root == None:
            return 0
        ans, stack = 0, [(root, 0)]
        while stack:
            node, num = stack.pop()
            num += node.val
            if node.left == None and node.right == None:
                ans += num
            if node.left:
                stack.append((node.left, num * 10))
            if node.right:
                stack.append((node.right, num * 10))
        return ans


