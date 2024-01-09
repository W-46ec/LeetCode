
"""
# Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence**.
![872_tree](./img/872_tree.png)


For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.


**Example 1:** 
![872_leaf-similar-1](./img/872_leaf-similar-1.jpg)
```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```

**Example 2:** 
![872_leaf-similar-2](./img/872_leaf-similar-2.jpg)
```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

**Constraints:** 
    - The number of nodes in each tree will be in the range `[1, 200]`.
    - Both of the given trees will have values in the range `[0, 200]`.
"""

import sys
sys.path += ['.', '../', '../../']

import unittest
from util import TreeNode, deserializeTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _leaf_val_seq(self, root: Optional[TreeNode]) -> List[int]:
        stack, curr, sequence = [], root, []
        while curr or stack:
            while curr != None:
                stack += [curr]
                curr = curr.left
            node = stack.pop()
            sequence += [node.val] if node.left == None and node.right == None else []
            curr = node.right
        return sequence

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self._leaf_val_seq(root1) == self._leaf_val_seq(root2)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.leafSimilar(deserializeTree("[3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]"), deserializeTree("[3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]")), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.leafSimilar(deserializeTree("[1, 2, 3]"), deserializeTree("[1, 3, 2]")), False)

    def testcase3(self):
        self.assertEqual(self.soln_obj.leafSimilar(deserializeTree("[1]"), deserializeTree("[1]")), True)

    def testcase4(self):
        self.assertEqual(self.soln_obj.leafSimilar(deserializeTree("[1]"), deserializeTree("[2]")), False)


if __name__ == '__main__':
    unittest.main()
