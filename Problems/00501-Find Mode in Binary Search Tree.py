
"""
# Find Mode in Binary Search Tree

Given the `root` of a binary search tree (BST) with duplicates, return *all the [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) (i.e., the most frequently occurred element) in it*.

If the tree has more than one mode, return them in **any order**.

Assume a BST is defined as follows:
    - The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
    - The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
    - Both the left and right subtrees must also be binary search trees.


**Example 1:** 
![501_mode-tree](./img/501_mode-tree.jpg)
```
Input: root = [1,null,2,2]
Output: [2]
```

**Example 2:** 
```
Input: root = [0]
Output: [0]
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-10^5 <= Node.val <= 10^5` 


**Follow up**: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

import sys
sys.path += ['.', '../', '../../'] 

import unittest
from random import randint
from typing import List, Optional
from util import TreeNode, deserializeTree
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def inorder(tree: Optional[TreeNode]) -> None:
            if tree:
                inorder(tree.left)
                freq[tree.val] += 1
                inorder(tree.right)

        inorder(root)
        max_freq = max(freq.values())
        return [k for k in freq if freq[k] == max_freq]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findMode(deserializeTree("[1, null, 2, 2]")), [2])

    def testcase2(self):
        self.assertEqual(self.soln_obj.findMode(deserializeTree("[0]")), [0])

    def testcase3(self):
        self.assertEqual(self.soln_obj.findMode(deserializeTree("[1, 1, 2, null, null, 2]")), [1, 2])


if __name__ == '__main__':
    unittest.main()
