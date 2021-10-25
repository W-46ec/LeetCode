
"""
# Cousins in Binary Tree

Given the `root` of a binary tree with unique values and the values of two different nodes of the tree `x` and `y`, return `true` *if the nodes corresponding to the values `x` and `y` in the tree are **cousins**, or `false` otherwise*.

Two nodes of a binary tree are **cousins** if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth `0`, and children of each depth `k` node are at the depth `k + 1`.

**Example 1:** 
![993_q1248-01](./img/993_q1248-01.png)
```
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
```

**Example 2:** 
![993_q1248-02](./img/993_q1248-02.png)
```
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
```

**Example 3:** 
![993_q1248-03](./img/993_q1248-03.png)
```
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[2, 100]`.
    - `1 <= Node.val <= 100` 
    - Each node has a **unique** value.
    - `x != y` 
    - `x` and `y` are exist in the tree.
"""

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        target1, target2 = None, None
        def dfs(tree, parent = None, depth = 0):
            nonlocal target1, target2
            if tree == None:
                return
            if tree.val == x:
                target1 = (parent, depth)
            elif tree.val == y:
                target2 = (parent, depth)
            dfs(tree.left, tree, depth + 1)
            dfs(tree.right, tree, depth + 1)
        dfs(root)
        return target1[0] != target2[0] and target1[1] == target2[1]

# False
print(Solution().isCousins(deserializeTree("[1, 2, 3, 4]"), 4, 3))

# True
print(Solution().isCousins(deserializeTree("[1, 2, 3, null, 4, null, 5]"), 5, 4))

# False
print(Solution().isCousins(deserializeTree("[1, 2, 3, null, 4]"), 2, 3))
