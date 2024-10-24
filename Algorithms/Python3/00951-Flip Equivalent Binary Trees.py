
"""
# Flip Equivalent Binary Trees

For a binary tree **T**, we can define a **flip operation** as follows: choose any node, and swap the left and right child subtrees.

A binary tree **X** is *flip equivalent* to a binary tree **Y** if and only if we can make **X** equal to **Y** after some number of flip operations.

Given the roots of two binary trees `root1` and `root2`, return `true` if the two trees are flip equivalent or `false` otherwise.


**Example 1:** 
![951_tree_ex](./img/951_tree_ex.png)
```
Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
```

**Example 2:** 
```
Input: root1 = [], root2 = []
Output: true
```

**Example 3:** 
```
Input: root1 = [], root2 = [1]
Output: false
```

**Constraints:** 
    - The number of nodes in each tree is in the range `[0, 100]`.
    - Each tree will have **unique node values** in the range `[0, 99]`.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from util import TreeNode, deserializeTree
import unittest
from typing import Optional

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Run DFS on both trees simultaneously
        stack1, stack2 = [root1] if root1 else [], [root2] if root2 else []
        while stack1 and stack2:
            node1, node2 = stack1.pop(), stack2.pop()
            if node1.val != node2.val:
                return False
            l1 = node1.left.val if node1.left else None
            l2 = node2.left.val if node2.left else None
            r1 = node1.right.val if node1.right else None
            r2 = node2.right.val if node2.right else None
            if (l1, r1) != (l2, r2) and (l1, r1) != (r2, l2):
                return False
            stack1 += [node1.left] if node1.left else []
            stack1 += [node1.right] if node1.right else []
            if l1 == l2:
                stack2 += [node2.left] if node2.left else []
                stack2 += [node2.right] if node2.right else []
            else:
                stack2 += [node2.right] if node2.right else []
                stack2 += [node2.left] if node2.left else []
        return stack1 == stack2


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        ans = self.soln_obj.flipEquiv(
            deserializeTree("[1, 2, 3, 4, 5, 6, null, null, null, 7, 8]"), 
            deserializeTree("[1, 3, 2, null, 6, 4, 5, null, null, null, null, 8, 7]")
        )
        self.assertEqual(ans, True)

    def testcase2(self):
        ans = self.soln_obj.flipEquiv(
            deserializeTree("[]"), 
            deserializeTree("[]")
        )
        self.assertEqual(ans, True)

    def testcase3(self):
        ans = self.soln_obj.flipEquiv(
            deserializeTree("[]"), 
            deserializeTree("[1]")
        )
        self.assertEqual(ans, False)

    def testcase4(self):
        ans = self.soln_obj.flipEquiv(
            deserializeTree("[1]"), 
            deserializeTree("[1]")
        )
        self.assertEqual(ans, True)

    def testcase5(self):
        ans = self.soln_obj.flipEquiv(
            deserializeTree("[1, 2]"), 
            deserializeTree("[1, null, 2]")
        )
        self.assertEqual(ans, True)

    def testcase6(self):
        ans = self.soln_obj.flipEquiv(
            deserializeTree("[0, 2, 1, 4, null, 3, 5, null, null, 6, 7]"), 
            deserializeTree("[0, 2, 1, 4, null, 3, 5, null, null, null, 6, 7]")
        )
        self.assertEqual(ans, False)


if __name__ == '__main__':
    unittest.main()
