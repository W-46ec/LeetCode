
"""
# Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

**Example 1:** 
```
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
```

**Note:** 
    1. The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree
from typing import List
from collections import defaultdict

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue = [(0, root)]
        val_map, num_map = defaultdict(int), defaultdict(int)
        for lv, node in queue:
            val_map[lv] += node.val
            num_map[lv] += 1
            queue += [(lv + 1, node.left)] if node.left else []
            queue += [(lv + 1, node.right)] if node.right else []
        return [val_map[lv] / num_map[lv] for lv in val_map]

# [3.00000,14.50000,11.00000]
print(Solution().averageOfLevels(deserializeTree("[3, 9, 20, 15, 7]")))

