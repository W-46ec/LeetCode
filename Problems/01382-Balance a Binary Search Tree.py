
"""
# Balance a Binary Search Tree

Given the `root` of a binary search tree, return *a **balanced** binary search tree with the same node values*. If there is more than one answer, return **any of them**.

A binary search tree is **balanced** if the depth of the two subtrees of every node never differs by more than `1`.


**Example 1:** 
![1382_balance1-tree](./img/1382_balance1-tree.jpg)
```
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
```

**Example 2:** 
![1382_balanced2-tree](./img/1382_balanced2-tree.jpg)
```
Input: root = [2,1,3]
Output: [2,1,3]
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `1 <= Node.val <= 10^5` 
"""

import sys
sys.path += ['.', '../', '../../']

from util import TreeNode, deserializeTree, serializeTree
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Recover the sorted list of elements from the existing BST by inorder traversal.
        And then construct a new balanced BST using divide-and-conquer approach.

        By the definition of BST, for any node v on the tree, the values of nodes in its left
        subtree should be less than the value of v. And the values of nodes in its right subtree
        should be greater than the value of v.

        Therefore, if we want the tree to be balanced, we want roughly the same number of nodes in
        both of left and right subtrees. So choosing the middle node in the sorted list to be the
        root node would be a good idea. And then apply the same strategy for both halves of the list.
        """

        # # Recursive inorder traversal
        # def inorder(tree: TreeNode, nums: List[int]) -> None:
        #     if not tree:
        #         return
        #     inorder(tree.left, nums)
        #     nums.append(tree.val)
        #     inorder(tree.right, nums)

        # Iterative inorder traversal
        stack, nums = [root], []
        while stack:
            while stack[-1].left:
                stack += [stack[-1].left]
            node = stack.pop()
            nums += [node.val]
            while stack and not node.right:
                node = stack.pop()
                nums += [node.val]
            stack += [node.right] if node.right else []

        def _buildTree(nums: List[int], lo: int, hi: int) -> TreeNode:
            if lo <= hi:
                mid = (lo + hi) // 2;
                return TreeNode(nums[mid], _buildTree(nums, lo, mid - 1), _buildTree(nums, mid + 1, hi))
            return None

        return _buildTree(nums, 0, len(nums) - 1)


# [2, 1, 3, null, null, null, 4]
print(serializeTree(Solution().balanceBST(deserializeTree("[1, null, 2, null, 3, null, 4, null, null]"))))

# [2, 1, 3]
print(serializeTree(Solution().balanceBST(deserializeTree("[2, 1, 3]"))))

# [2, 1, 3, null, null, null, 4]
print(serializeTree(Solution().balanceBST(deserializeTree("[1, null, 2, null, 3, null, 4]"))))
