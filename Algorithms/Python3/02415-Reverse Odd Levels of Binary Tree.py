
"""
# Reverse Odd Levels of Binary Tree

Given the `root` of a **perfect** binary tree, reverse the node values at each **odd** level of the tree.

- For example, suppose the node values at level 3 are `[2,1,3,4,7,11,29,18]`, then it should become `[18,29,11,7,4,3,1,2]`.

Return *the root of the reversed tree*.

A binary tree is **perfect** if all parent nodes have two children and all leaves are on the same level.

The **level** of a node is the number of edges along the path between it and the root node.


**Example 1:** 
![2415_first_case1](./img/2415_first_case1.png)
```
Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]
Explanation: 
The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.
```

**Example 2:** 
![2415_second_case3](./img/2415_second_case3.png)
```
Input: root = [7,13,11]
Output: [7,11,13]
Explanation: 
The nodes at level 1 are 13, 11, which are reversed and become 11, 13.
```

**Example 3:** 
```
Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
Explanation: 
The odd levels have non-zero values.
The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 2^14]`.
    - `0 <= Node.val <= 10^5` 
    - `root` is a **perfect** binary tree.
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue, node_dict = [(root, 0)], defaultdict(list)
        while queue:
            node, level = queue.pop(0)
            queue += [(node.left, level + 1)] if node.left else []
            queue += [(node.right, level + 1)] if node.right else []
            if level % 2:
                node_dict[level] = [node.val] + node_dict[level]
            else:
                node_dict[level] += [node.val]

        nodes = []
        for lv in range(max(node_dict.keys()) + 1):
            nodes += node_dict[lv]
        
        root_reversed = TreeNode(nodes[0])
        stack = [(root_reversed, 0)]
        while stack:
            node, idx = stack.pop()
            if 2 * idx + 1 < len(nodes):
                node.left = TreeNode(nodes[2 * idx + 1])
                stack += [(node.left, 2 * idx + 1)]
            if 2 * idx + 2 < len(nodes):
                node.right = TreeNode(nodes[2 * idx + 2])
                stack += [(node.right, 2 * idx + 2)]
        return root_reversed


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        ans = serializeTree(self.soln_obj.reverseOddLevels(deserializeTree("[2, 3, 5, 8, 13, 21, 34]")))
        expected = "[2, 5, 3, 8, 13, 21, 34]"
        self.assertEqual(ans, expected)

    def testcase2(self):
        ans = serializeTree(self.soln_obj.reverseOddLevels(deserializeTree("[7, 13, 11]")))
        expected = "[7, 11, 13]"
        self.assertEqual(ans, expected)

    def testcase3(self):
        ans = serializeTree(self.soln_obj.reverseOddLevels(deserializeTree("[0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]")))
        expected = "[0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]"
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
