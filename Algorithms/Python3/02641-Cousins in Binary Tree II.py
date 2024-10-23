
"""
# Cousins in Binary Tree II

Given the `root` of a binary tree, replace the value of each node in the tree with the **sum of all its cousins' values**.

Two nodes of a binary tree are **cousins** if they have the same depth with different parents.

Return *the `root` of the modified tree*.

**Note** that the depth of a node is the number of edges in the path from the root node to it.


**Example 1:** 
![2641_example11](./img/2641_example11.png)
```
Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
```

**Example 2:** 
![2641_diagram33](./img/2641_diagram33.png)
```
Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^5]`.
    - `1 <= Node.val <= 10^4` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from util import TreeNode, serializeTree, deserializeTree
import unittest
from typing import Optional
from collections import defaultdict

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Run BFS to compute level sums
        queue, level_sum = [(root, 0)], defaultdict(int)
        while queue:
            node, level = queue.pop(0)
            level_sum[level] += node.val
            queue += [(node.left, level + 1)] if node.left else []
            queue += [(node.right, level + 1)] if node.right else []

        # Run DFS to create a new tree and compute the modified values
        modified_root = TreeNode(root.val, None, None)
        stack = [(root, modified_root, root.val, 0)]
        while stack:
            node, modified_node, curr_sibling_sum, level = stack.pop()
            modified_node.val = level_sum[level] - curr_sibling_sum
            nxt_sibling_sum = node.left.val if node.left else 0
            nxt_sibling_sum += node.right.val if node.right else 0
            if node.left:
                modified_node.left = TreeNode(node.left.val)
                stack += [(node.left, modified_node.left, nxt_sibling_sum, level + 1)]
            if node.right:
                modified_node.right = TreeNode(node.right.val)
                stack += [(node.right, modified_node.right, nxt_sibling_sum, level + 1)]
        return modified_root


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        ans = serializeTree(self.soln_obj.replaceValueInTree(deserializeTree("[5, 4, 9, 1, 10, null, 7]")))
        expected = "[0, 0, 0, 7, 7, null, 11]"
        self.assertEqual(ans, expected)

    def testcase2(self):
        ans = serializeTree(self.soln_obj.replaceValueInTree(deserializeTree("[3, 1, 2]")))
        expected = "[0, 0, 0]"
        self.assertEqual(ans, expected)

    def testcase3(self):
        ans = serializeTree(self.soln_obj.replaceValueInTree(deserializeTree("[5]")))
        expected = "[0]"
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
