
"""
# Step-By-Step Directions From a Binary Tree Node to Another

You are given the `root` of a **binary tree** with `n` nodes. Each node is uniquely assigned a value from `1` to `n`. You are also given an integer `startValue` representing the value of the start node `s`, and a different integer `destValue` representing the value of the destination node `t`.

Find the **shortest path** starting from node `s` and ending at node `t`. Generate step-by-step directions of such path as a string consisting of only the **uppercase** letters `'L'`, `'R'`, and `'U'`. Each letter indicates a specific direction:
    - `'L'` means to go from a node to its **left child** node.
    - `'R'` means to go from a node to its **right child** node.
    - `'U'` means to go from a node to its **parent** node.

Return *the step-by-step directions of the **shortest path** from node `s` to node `t`*.


**Example 1:** 
![2096_eg1](./img/2096_eg1.png)
```
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
```

**Example 2:** 
![2096_eg2](./img/2096_eg2.png)
```
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
```

**Constraints:** 
    - The number of nodes in the tree is `n`.
    - `2 <= n <= 10^5` 
    - `1 <= Node.val <= n` 
    - All the values in the tree are **unique**.
    - `1 <= startValue, destValue <= n` 
    - `startValue != destValue` 
"""

import sys
sys.path += ['.', '../', '../../']

from util import TreeNode, deserializeTree
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def postorder(tree, target, path):
            if tree:
                if tree.val == target:
                    path.insert(0, tree)
                    return True
                if postorder(tree.left, target, path) \
                        or postorder(tree.right, target, path):
                    path.insert(0, tree)
                    return True
            return False

        path_start, path_dest = [], []
        postorder(root, startValue, path_start)
        postorder(root, destValue, path_dest)

        common_prefix_len = 0
        while common_prefix_len < len(path_start) \
                and common_prefix_len < len(path_dest) \
                and path_start[common_prefix_len] == path_dest[common_prefix_len]:
            common_prefix_len += 1

        directions = 'U' * (len(path_start) - common_prefix_len)
        for i in range(common_prefix_len - 1, len(path_dest) - 1):
            directions += 'L' if path_dest[i + 1] == path_dest[i].left else 'R'

        return directions

# UURL
print(Solution().getDirections(deserializeTree("[5, 1, 2, 3, null, 6, 4]"), 3, 6))

# L
print(Solution().getDirections(deserializeTree("[2, 1]"), 2, 1))

# U
print(Solution().getDirections(deserializeTree("[2, 1]"), 1, 2))

# UR
print(Solution().getDirections(deserializeTree("[1, 2, null, 3, 4]"), 3, 4))
