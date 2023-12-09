
"""
# Binary Tree Inorder Traversal

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.


**Example 1:** 
![094_inorder_1](./img/094_inorder_1.jpg)
```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

**Example 2:** 
```
Input: root = []
Output: []
```

**Example 3:** 
```
Input: root = [1]
Output: [1]
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100` 

**Follow up**: Recursive solution is trivial, could you do it iteratively?
"""

import sys
sys.path += ['.', '../', '../../']

import unittest
from util import TreeNode, deserializeTree
from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # Recursive solution
        # if root:
        #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # return []

        # Iterative solution
        stack, curr_node, arr = [], root, []
        while curr_node or stack:
            while curr_node:
                stack += [curr_node]
                curr_node = curr_node.left
            node = stack.pop()
            arr += [node.val]
            curr_node = node.right
        return arr


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.inorderTraversal(deserializeTree("[1, null, 2, 3]")), [1, 3, 2])

    def testcase2(self):
        self.assertEqual(self.soln_obj.inorderTraversal(deserializeTree("[]")), [])

    def testcase3(self):
        self.assertEqual(self.soln_obj.inorderTraversal(deserializeTree("[1]")), [1])


if __name__ == '__main__':
    unittest.main()
