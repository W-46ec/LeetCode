
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
![13_116_sample](./img/13_116_sample.png)
```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

**Constraints:** 
    - The number of nodes in the given tree is less than `4096`.
    - `-1000 <= node.val <= 1000` 
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [(0, root)]
        for level, node in queue:
            queue += [(level + 1, node.left)] if node.left else []
            queue += [(level + 1, node.right)] if node.right else []
        for i in range(len(queue) - 1):
            queue[i][1].next = queue[i + 1][1] if queue[i][0] == queue[i + 1][0] else None
        return queue[0][1]

