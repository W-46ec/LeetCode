
"""
# Vertical Order Traversal of a Binary Tree

Given a binary tree, return the *vertical order* traversal of its nodes values.

For each node at position `(X, Y)`, its left and right children respectively will be at positions `(X-1, Y-1)` and `(X+1, Y-1)`.

Running a vertical line from `X = -infinity` to `X = +infinity`, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing `Y` coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of `X` coordinate. Every report will have a list of values of nodes.


**Example 1:** 

```
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
```

**Example 2:** 

```
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
```

**Note:** 
    1. The tree will have between 1 and `1000` nodes.
    2. Each node's value will be between `0` and `1000`.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path.append('../../')

from typing import List
from util import TreeNode, initTree

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        left, right = [], []
        def traverse(tree, offset = 0, level = 0):
            nonlocal left, right
            if not tree:
                return
            if offset >= 0 and len(right) - offset <= 0:
                right += [[]]
            if offset < 0 and len(left) + offset < 0:
                left = [[]] + left

            if offset >= 0:
                right[offset].append((level, tree.val))
            else:
                left[offset].append((level, tree.val))
            traverse(tree.left, offset - 1, level + 1)
            traverse(tree.right, offset + 1, level + 1)
        traverse(root)
        return list(map(lambda lst: [x[1] for x in lst], 
                        map(lambda lst: sorted(lst), left + right)))

# # Testcases
# [3,9,20,null,null,15,7]
# [1,2,3,4,5,6,7]
# [0,null,1,2,3,null,null,4,5]
# [0,8,1,null,null,3,2,null,4,5,null,null,7,6]
# [0,1,null,null,2,6,3,null,null,null,4,null,5]
# [0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]

# # ANS
# [[9],[3,15],[20],[7]]
# [[4],[2],[1,5,6],[3],[7]]
# [[0,2],[1,4],[3],[5]]
# [[8],[0,3,6],[1,4,5],[2,7]]
# [[1,6],[0,2],[3],[4],[5]]
# [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]]

print(Solution().verticalTraversal(initTree([3, 9, 20, None, None, 15, 7])))
print(Solution().verticalTraversal(initTree([1, 2, 3, 4, 5, 6, 7])))
print(Solution().verticalTraversal(initTree([0, None, 1, 2, 3, None, None, 4, 5])))
print(Solution().verticalTraversal(initTree([0, 8, 1, None, None, 3, 2, None, 4, 5, None, None, 7, 6])))
print(Solution().verticalTraversal(initTree([0, 1, None, None, 2, 6, 3, None, None, None, 4, None, 5])))
print(Solution().verticalTraversal(initTree([0, 2, 1, 3, None, None, None, 4, 5, None, 7, 6, None, 10, 8, 11, 9])))

