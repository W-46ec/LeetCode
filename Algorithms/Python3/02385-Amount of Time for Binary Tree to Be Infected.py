
"""
# Amount of Time for Binary Tree to Be Infected

You are given the `root` of a binary tree with unique values, and an integer `start`. At minute `0`, an **infection** starts from the node with value `start`.

Each minute, a node becomes infected if:
    - The node is currently uninfected.
    - The node is adjacent to an infected node.

Return *the number of minutes needed for the entire tree to be infected*.


**Example 1:** 
![2385_image-20220625231744-1](./img/2385_image-20220625231744-1.png)
```
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
```

**Example 2:** 
![2385_image-20220625231812-2](./img/2385_image-20220625231812-2.png)
```
Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^5]`.
    - 1 <= Node.val <= 10^5` 
    - Each node has a **unique** value.
    - A node with a value of `start` exists in the tree.
"""

import sys
sys.path += ['.', '../', '../../']

import unittest
from util import TreeNode, deserializeTree
from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Locate the start node
        # Turn the tree into an undirected graph using DFS
        graph, stack, start_node = defaultdict(list), [(root, None)], None
        while stack:
            node, parent = stack.pop()
            start_node = node.val if node.val == start else start_node
            stack += [(node.left, node)] if node.left else []
            stack += [(node.right, node)] if node.right else []
            graph[node.val] += [node.left.val] if node.left else []
            graph[node.val] += [node.right.val] if node.right else []
            graph[node.val] += [parent.val] if parent else []

        # Run BFS to traverse the graph
        # Start from the infected node
        queue, visited, total_time = [(start_node, 0)], {start_node}, 0
        while queue:
            src, time = queue.pop(0)
            total_time = max(total_time, time)
            for dst in graph[src]:
                if dst not in visited:
                    queue += [(dst, time + 1)]
                    visited.add(dst)

        return total_time


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.amountOfTime(deserializeTree("[1, 5, 3, null, 4, 10, 6, 9, 2]"), 3), 4)

    def testcase2(self):
        self.assertEqual(self.soln_obj.amountOfTime(deserializeTree("[1]"), 1), 0)


if __name__ == '__main__':
    unittest.main()
