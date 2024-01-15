
"""
# Construct String from Binary Tree

Given the `root` of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.


**Example 1:** 
![606_cons1-tree](./img/606_cons1-tree.jpg)
```
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
```

**Example 2:** 
![606_cons2-tree](./img/606_cons2-tree.jpg)
```
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-1000 <= Node.val <= 1000` 
"""

import sys
sys.path += ['.', '../', '../../']

import unittest
from util import TreeNode, deserializeTree
from typing import Optional

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = str(root.val)
        if root.left:
            s += "(%s)" % self.tree2str(root.left)
            s += "(%s)" % self.tree2str(root.right) if root.right else ""
        else:
            if root.right:
                s += "()(%s)" % self.tree2str(root.right)
        return s


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.tree2str(deserializeTree("[1, 2, 3, 4]")), "1(2(4))(3)")

    def testcase2(self):
        self.assertEqual(self.soln_obj.tree2str(deserializeTree("[1, 2, 3, null, 4]")), "1(2()(4))(3)")

    def testcase3(self):
        self.assertEqual(self.soln_obj.tree2str(deserializeTree("[1]")), "1")

    def testcase4(self):
        self.assertEqual(self.soln_obj.tree2str(deserializeTree("[1, null, 2]")), "1()(2)")

    def testcase5(self):
        self.assertEqual(self.soln_obj.tree2str(deserializeTree("[1, null, 2, null, 3]")), "1()(2()(3))")


if __name__ == '__main__':
    unittest.main()
