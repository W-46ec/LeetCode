
"""
# Count Complete Tree Nodes

Given a **complete** binary tree, count the number of nodes.

**Note:** 

**Definition of a complete binary tree from Wikipedia:** 
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

**Example:** 
```
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # # O(n) solution
        # if not root:
        #     return 0
        # tree, ans = root, 0
        # Q = [tree]
        # while Q:
        #     node = Q.pop(0)
        #     ans += 1
        #     if node.left:
        #         Q.append(node.left)
        #     if node.right:
        #         Q.append(node.right)
        # return ans

        # O(logn * logn) solution
        # Reference: https://leetcode.com/problems/count-complete-tree-nodes/discuss/701392/Two-Solution-or-Simple-0(logn-*-logn)-and-1-liner-recursive-O(n)
        def countHeight(tree):
            lh, rh = 0, 0
            ltree, rtree = tree, tree
            while ltree or rtree:
                if ltree:
                    lh += 1
                    ltree = ltree.left
                if rtree:
                    rh += 1
                    rtree = rtree.right
            return lh, rh
        ans, Q = 0, [root]
        while Q:
            node = Q.pop(0)
            lh, rh = countHeight(node)
            if lh == rh:
                ans += 2 ** lh - 1
            else:
                ans += 1
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return ans
            


