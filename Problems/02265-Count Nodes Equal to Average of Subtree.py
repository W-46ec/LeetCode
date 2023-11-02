
"""
# Count Nodes Equal to Average of Subtree

Given the `root` of a binary tree, return the *number of nodes where the value of the node is equal to the **average** of the values in its **subtree***.

**Note:** 
    - The **average** of `n` elements is the **sum** of the `n` elements divided by `n` and **rounded down** to the nearest integer.
    - A **subtree** of `root` is a tree consisting of `root` and all of its descendants.


**Example 1:** 
![2265_image-20220315203925-1](./img/2265_image-20220315203925-1.png)
```
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
```

**Example 2:** 
![2265_image-20220326133920-1](./img/2265_image-20220326133920-1.png)
```
Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
```

**Constraints:** 
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 1000
"""

import sys
sys.path += ['.', '../', '../../'] 

import unittest
from typing import Tuple, Optional
from util import TreeNode, deserializeTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def postorder(tree: Optional[TreeNode]) -> Tuple[int]:
            nonlocal count
            if tree:
                l_num_nodes, l_val_sum = postorder(tree.left)
                r_num_nodes, r_val_sum = postorder(tree.right)
                num_nodes = l_num_nodes + r_num_nodes + 1
                val_sum = tree.val + l_val_sum + r_val_sum
                count += 1 if val_sum // num_nodes == tree.val else 0
                return (num_nodes, val_sum)
            return (0, 0)

        postorder(root)
        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.averageOfSubtree(deserializeTree("[4, 8, 5, 0, 1, null, 6]")), 5)

    def testcase2(self):
        self.assertEqual(self.soln_obj.averageOfSubtree(deserializeTree("[1]")), 1)


if __name__ == '__main__':
    unittest.main()