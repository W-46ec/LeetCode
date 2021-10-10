
"""
# Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the *zigzag level order* traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```

return its zigzag level order traversal as:
```
[
  [3],
  [20,9],
  [15,7]
]
```
"""

from typing import List
from util import TreeNode, initTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
            else:   # New level
                ans.append([node.val])
            queue += [(node.left, level + 1)] if node.left else []
            queue += [(node.right, level + 1)] if node.right else []
        return ans


# [[3], [20, 9], [15, 7]]
print(Solution().zigzagLevelOrder(initTree([3, 9, 20, None, None, 15, 7])))

