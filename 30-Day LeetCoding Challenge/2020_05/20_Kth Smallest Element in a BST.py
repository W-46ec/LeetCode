
"""
# Kth Smallest Element in a BST

Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.

**Note:** 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

**Example 1:** 
```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2:** 
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

**Follow up:** 
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # # O(N) solution - Recursion
        # ans = []
        # def inOrder(tree):
        #     if not tree or len(ans) >= k:
        #         return
        #     inOrder(tree.left)
        #     ans.append(tree.val)
        #     inOrder(tree.right)
        # inOrder(root)
        # return ans[k - 1]

        # O(Height + k) solution
        # Adapted from https://leetcode.com/articles/kth-smallest-element-in-a-bst/
        stack, tree = [], root
        while True:
            while tree:
                stack.append(tree)
                tree = tree.left
            tree = stack.pop()
            k -= 1
            if k <= 0:
                return tree.val
            tree = tree.right


