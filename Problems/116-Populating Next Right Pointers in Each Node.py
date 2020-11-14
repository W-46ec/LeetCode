
"""
# Populating Next Right Pointers in Each Node

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.


**Follow up:** 
    - You may only use constant extra space.
    - Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


**Example 1:** 
![116_sample](./img/116_sample.png)
```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

**Constraints:** 
    - The number of nodes in the given tree is less than `4096`.
    - `-1000 <= node.val <= 1000` 
"""

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def initTree(lst: List) -> Node:
    if not lst:
        return None
    root = Node(lst.pop(0))
    Q = [root]
    while Q:
        node = Q.pop(0)
        if lst:
            val = lst.pop(0)
            node.left = Node(val) if val != None else None
            Q += [node.left] if node.left else []
        if lst:
            val = lst.pop(0)
            node.right = Node(val) if val != None else None
            Q += [node.right] if node.right else []
    return root

def printSoln(root):
    lst = []
    while root:
        node = root
        while node:
            lst, node = lst + [node.val], node.next
        lst += ['#']
        root = root.left
    print(lst)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # # O(n) space
        # if not root:
        #     return None
        # queue = [(0, root)]
        # for level, node in queue:
        #     queue += [(level + 1, node.left)] if node.left else []
        #     queue += [(level + 1, node.right)] if node.right else []
        # for i in range(len(queue) - 1):
        #     queue[i][1].next = queue[i + 1][1] if queue[i][0] == queue[i + 1][0] else None
        # return queue[0][1]
        
        # O(1) space
        if root and root.left:  # Within subtree
            root.left.next = root.right
            if root.next:       # Between subtrees
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root

# [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']
printSoln(Solution().connect(initTree([1, 2, 3, 4, 5, 6, 7])))

