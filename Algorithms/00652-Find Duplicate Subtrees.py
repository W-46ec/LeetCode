
"""
# Find Duplicate Subtrees

Given the `root` of a binary tree, return all **duplicate subtrees**.

For each kind of duplicate subtrees, you only need to return the root node of any **one** of them.

Two trees are **duplicate** if they have the **same structure** with the **same node values**.

**Example 1:** 
![652_e1](./img/652_e1.jpg)
```
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
```

**Example 2:** 
![652_e2](./img/652_e2.jpg)
```
Input: root = [2,1,1]
Output: [[1]]
```

**Example 3:** 
![652_e33](./img/652_e33.jpg)
```
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
```

**Constraints:** 
    - The number of the nodes in the tree will be in the range `[1, 5000]` 
    - `-200 <= Node.val <= 200` 
"""

import sys
sys.path += ['.', '../', '../../']

from typing import List, Optional
from util import TreeNode, deserializeTree, serializeTree
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Run DFS to traverse the tree
        # In the meanwhile, serialize every subtree from bottom to top
        # Use a hashmap to record the occurance of each subtree

        ans, counter = [], defaultdict(int)

        def dfs(node):
            nonlocal ans
            if not node:
                return '{}'
            left_str, right_str = dfs(node.left), dfs(node.right)
            tree_str = "{%d: [%s, %s]}" % (node.val, left_str, right_str)
            counter[tree_str] += 1
            ans += [node] if counter[tree_str] == 2 else []
            return tree_str

        dfs(root)
        return ans

# [[4], [2, 4]]
print([eval(serializeTree(tree)) for tree in Solution().findDuplicateSubtrees(deserializeTree("[1, 2, 3, 4, null, 2, 4, null, null, 4]"))])

# [[1]]
print([eval(serializeTree(tree)) for tree in Solution().findDuplicateSubtrees(deserializeTree("[2, 1, 1]"))])

# [[3], [2, 3]]
print([eval(serializeTree(tree)) for tree in Solution().findDuplicateSubtrees(deserializeTree("[2, 2, 2, 3, null, 3, null]"))])
