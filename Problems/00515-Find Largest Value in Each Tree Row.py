
"""
# Find Largest Value in Each Tree Row

Given the `root` of a binary tree, return *an array of the largest value in each row* of the tree (**0-indexed**).


**Example 1:** 
![515_largest_e1](./img/515_largest_e1.jpg)
```
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
```

**Example 2:** 
```
Input: root = [1,2,3]
Output: [1,3]
```

**Constraints:** 
    - The number of nodes in the tree will be in the range `[0, 10^4]`.
    - `-2^31 <= Node.val <= 2^31 - 1` 
"""

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        max_vals = []
        if root:
            queue = [(0, root)]
            while queue:
                level, node = queue.pop(0)
                if level >= len(max_vals):
                    max_vals += [node.val]
                else:
                    max_vals[level] = max(max_vals[level], node.val)
                queue += [(level + 1, node.left)] if node.left else []
                queue += [(level + 1, node.right)] if node.right else []
        return max_vals

# [1, 3, 9]
print(Solution().largestValues(deserializeTree("[1, 3, 2, 5, 3, null, 9]")))

# [1, 3]
print(Solution().largestValues(deserializeTree("[1, 2, 3]")))
