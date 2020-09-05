
"""
# All Elements in Two Binary Search Trees

Given two binary search trees `root1` and `root2`.

Return a list containing *all the integers* from *both trees* sorted in **ascending** order.


**Example 1:** 
![05_q2-e1](./img/05_q2-e1.png)
```
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
```

**Example 2:** 
```
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
```

**Example 3:** 
```
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
```

**Example 4:** 
```
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
```

**Example 5:** 
![05_q2-e2](./img/05_q2-e2.png)
```
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
```

**Constraints:** 
    - Each tree has at most `5000` nodes.
    - Each node's value is between `[-10^5, 10^5]`.

**Hint #1** 
Traverse the first tree in list1 and the second tree in list2.

**Hint #2** 
Merge the two trees in one list and sort it.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path = ['.', '../', '../../'] + sys.path

from typing import List
from util import TreeNode, initTree

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst, lst1, lst2 = [], [], []

        # Pre-order traversal
        def traverse(tree, lst):
            if not tree:
                return
            if tree.left:
                traverse(tree.left, lst)
            lst.append(tree.val)
            if tree.right:
                traverse(tree.right, lst)

        # Traverse both trees
        traverse(root1, lst1)
        traverse(root2, lst2)

        # Merge
        while lst1 and lst2:
            lst += [lst1.pop(0)] if lst1[0] < lst2[0] else [lst2.pop(0)]

        return lst + lst1 + lst2

# [0, 1, 1, 2, 3, 4]
print(Solution().getAllElements(initTree([2, 1, 4]), initTree([1, 0, 3])))

# [-10, 0, 0, 1, 2, 5, 7, 10]
print(Solution().getAllElements(initTree([0, -10, 10]), initTree([5, 1, 7, 0, 2])))

# [0, 1, 2, 5, 7]
print(Solution().getAllElements(initTree([]), initTree([5, 1, 7, 0, 2])))

# [-10, 0, 10]
print(Solution().getAllElements(initTree([0, -10, 10]), initTree([])))
