
"""
# Maximum Level Sum of a Binary Tree

Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the **smallest** level `x` such that the sum of all the values of nodes at level `x` is **maximal**.


**Example 1:** 
![1161_capture](./img/1161_capture.jfif)
```
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
```

**Example 2:** 
```
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-10^5 <= Node.val <= 10^5` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path += ['.', '../', '../../']

from typing import List, Optional
from util import TreeNode, deserializeTree
from collections import defaultdict

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums = defaultdict(int)
        queue = [(root, 1)] # node, level
        for node, level in queue:
            level_sums[level] += node.val
            queue += [(node.left, level + 1)] if node.left else []
            queue += [(node.right, level + 1)] if node.right else []
        # Note that we want the smallest level when multiple levels have the same sum
        return -max([(level_sums[level], -level) for level in level_sums])[1]

# 2
print(Solution().maxLevelSum(deserializeTree("[1, 7, 0, 7, -8, null, null]")))

# 2
print(Solution().maxLevelSum(deserializeTree("[989, null, 10250, 98693, -89388, null, null, null, -32127]")))

# 1
print(Solution().maxLevelSum(deserializeTree("[1, 1, 0, 7, -8, -7, 9]")))
