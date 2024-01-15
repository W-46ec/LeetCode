
"""
# Binary Tree Zigzag Level Order Traversal

Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).


**Example 1:** 
![103_tree1](./img/103_tree1.jpg)
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

**Example 2:** 
```
Input: root = [1]
Output: [[1]]
```

**Example 3:** 
```
Input: root = []
Output: []
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[0, 2000]`.
    - `-100 <= Node.val <= 100` 
"""

import sys
sys.path += ['.', '../', '../../'] 

from typing import List, Optional
from util import TreeNode, deserializeTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # O(2N)
        # if not root:
        #     return []

        # queue = [(0, root)]
        # for level, node in queue:
        #     queue += [(level + 1, node.left)] if node.left else []
        #     queue += [(level + 1, node.right)] if node.right else []

        # ans = [[] for _ in range(queue[-1][0] + 1)]
        # for level, node in queue:
        #     if level % 2 == 0:
        #         ans[level] += [node.val]
        #     else:
        #         ans[level] = [node.val] + ans[level]
        # return ans

        # O(N)
        if not root:
            return []
        queue, ans = [(root, 0)], []
        while queue:
            node, level = queue.pop(0)
            if len(ans) > level:
                if level % 2 == 0:  # left to right
                    ans[level].append(node.val)
                else:               # right to left
                    ans[level] = [node.val] + ans[level]
            else:                   # New level
                ans.append([node.val])
            queue += [(node.left, level + 1)] if node.left else []
            queue += [(node.right, level + 1)] if node.right else []
        return ans


# [[3], [20, 9], [15, 7]]
print(Solution().zigzagLevelOrder(deserializeTree("[3, 9, 20, null, null, 15, 7]")))

# [[1]]
print(Solution().zigzagLevelOrder(deserializeTree("[1]")))

# []
print(Solution().zigzagLevelOrder(deserializeTree("[]")))

