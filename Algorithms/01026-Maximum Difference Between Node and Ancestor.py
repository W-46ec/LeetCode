
"""
# Maximum Difference Between Node and Ancestor

Given the `root` of a binary tree, find the maximum value `v` for which there exist **different** nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any child of `a` is an ancestor of `b`.


**Example 1:** 
![1026_tmp-tree](./img/1026_tmp-tree.jpg)
```
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

**Example 2:** 
![1026_tmp-tree-1](./img/1026_tmp-tree-1.jpg)
```
Input: root = [1,null,2,null,0,3]
Output: 3
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[2, 5000]`.
    - `0 <= Node.val <= 10^5` 
"""

import sys
sys.path += ['.', '../', '../../']

import unittest
from util import TreeNode, deserializeTree
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Turn the tree into a directed graph such that
        # every node is pointing to its parent node and
        # the root node is pointing to None.
        directed_graph, queue, leaves = {}, [(root, None)], []
        while queue:
            node, parent = queue.pop(0)
            directed_graph[node] = parent
            queue += [(node.left, node)] if node.left else []
            queue += [(node.right, node)] if node.right else []
            leaves += [node] if not node.left and not node.right else []

        # Travel from each of the leaf node to the root node
        # and find out the min and max value along the path.
        max_diff = float('-inf')
        for leaf in leaves:
            curr_node, curr_min, curr_max = leaf, float('inf'), float('-inf')
            while curr_node:
                curr_min, curr_max = min(curr_min, curr_node.val), max(curr_max, curr_node.val)
                curr_node = directed_graph[curr_node]
            max_diff = max(max_diff, curr_max - curr_min)

        return max_diff


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.maxAncestorDiff(deserializeTree("[8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13]")), 7)

    def testcase2(self):
        self.assertEqual(self.soln_obj.maxAncestorDiff(deserializeTree("[1, null, 2, null, 0, 3]")), 3)


if __name__ == '__main__':
    unittest.main()
