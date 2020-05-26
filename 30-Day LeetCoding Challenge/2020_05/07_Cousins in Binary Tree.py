
"""
# Cousins in Binary Tree

In a binary tree, the root node is at depth `0`, and children of each depth `k` node are at depth `k+1`.

Two nodes of a binary tree are cousins if they have the same depth, but have **different parents.** 

We are given the `root` of a binary tree with unique values, and the values `x` and `y` of two different nodes in the tree.

Return `true` if and only if the nodes corresponding to the values `x` and `y` are cousins.


**Example 1:** 
![07_q1248-01](./img/07_q1248-01.png)
```
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
```

**Example 2:** 
![07_q1248-02](./img/07_q1248-02.png)
```
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
```

**Example 3:** 
![07_q1248-03](./img/07_q1248-03.png)
```
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
```

**Note:** 
    1. The number of nodes in the tree will be between `2` and `100`.
    2. Each node has a unique integer value from `1` to `100`.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        print(target1, target2)
        return target1[0] != target2[0] and target1[1] == target2[1]


