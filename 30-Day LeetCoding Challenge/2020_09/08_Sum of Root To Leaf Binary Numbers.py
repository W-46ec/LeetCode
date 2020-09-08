
"""
# Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value `0` or `1`.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.


**Example 1:** 

```
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

**Note:** 
    1. The number of nodes in the tree is between `1` and `1000`.
    2. node.val is `0` or `1`.
    3. The answer will not exceed `2^31 - 1`.

**Hint #1** 
Find each path, then transform that path to an integer in base 10.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import TreeNode, deserializeTree

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans, stack = 0, [(root, 0)]
        while stack:
            node, curr_sum = stack.pop()
            curr_sum += node.val
            ans += curr_sum if not node.left and not node.right else 0
            stack += [(node.left, curr_sum << 1)] if node.left else []
            stack += [(node.right, curr_sum << 1)] if node.right else []
        return ans

# 22
print(Solution().sumRootToLeaf(deserializeTree("[1, 0, 1, 0, 1, 0, 1]")))

