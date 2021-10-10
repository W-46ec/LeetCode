
"""
# Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

**Example 1:** 
```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

**Example 2:** 
```
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```

**Example 3:** 
```
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```
"""

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

from util import TreeNode, initTree

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif not p or not q:
            return False
        return p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)

p, q = initTree([1, 2, 3]), initTree([1, 2, 3])
print(Solution().isSameTree(p, q))  # True

p, q = initTree([1, 2]), initTree([1, None, 2])
print(Solution().isSameTree(p, q))  # False

p, q = initTree([1, 2, 1]), initTree([1, 1, 2])
print(Solution().isSameTree(p, q))  # False

