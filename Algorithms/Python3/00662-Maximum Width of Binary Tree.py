
"""
# Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a **full binary tree**, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the `null` nodes between the end-nodes are also counted into the length calculation.

**Example 1:** 
```
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```

**Example 2:** 
```
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```

**Example 3:** 

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```

**Example 4:** 
```
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
```

**Note:** Answer will in the range of 32-bit signed integer.
"""


# Reference: https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/726732/Python-10-lines-BFS-explained-with-figure

from util import initTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans, Q, curr_idx, curr_level = 0, [(0, 0, root)], 0, 0
        while Q:
            idx, level, node = Q.pop(0)
            if level == curr_level:
                ans = max(ans, idx - curr_idx + 1)
            else:
                curr_idx, curr_level = idx, level
            Q += [(idx * 2 + 1, level + 1, node.left)] if node.left else []
            Q += [(idx * 2 + 2, level + 1, node.right)] if node.right else []
        return ans

print(Solution().widthOfBinaryTree(initTree([1, 3, 2, 5, 3, None, 9]))) # 4
print(Solution().widthOfBinaryTree(initTree([1, 3, None, 5, 3])))       # 2
print(Solution().widthOfBinaryTree(initTree([1, 3, None, 5, 3])))       # 2
print(Solution().widthOfBinaryTree(initTree(
    [1, 3, 2, 5, None, None, 9, 6, None, None, None, None, None, None, 7]
)))     # 8
