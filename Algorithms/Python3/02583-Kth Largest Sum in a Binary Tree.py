
"""
# Kth Largest Sum in a Binary Tree

You are given the `root` of a binary tree and a positive integer `k`.

The **level sum** in the tree is the sum of the values of the nodes that are on the **same** level.

Return *the `kth` **largest** level sum in the tree (not necessarily distinct)*. If there are fewer than `k` levels in the tree, return `-1`.

**Note** that two nodes are on the same level if they have the same distance from the root.


**Example 1:** 
![2583_binaryytreeedrawio-2](./img/2583_binaryytreeedrawio-2.png)
```
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
```

**Example 2:** 
![2583_treedrawio-3](./img/2583_treedrawio-3.png)
```
Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
```

**Constraints:** 
    - The number of nodes in the tree is `n`.
    - `2 <= n <= 10^5` 
    - `1 <= Node.val <= 10^6` 
    - `1 <= k <= n` 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.path += ['.', '../', '../../']

from util import TreeNode, deserializeTree
import unittest
from typing import Optional
from collections import defaultdict

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue, level_sum = [(root, 0)], defaultdict(int)
        while queue:
            node, level = queue.pop(0)
            level_sum[level] += node.val
            queue += [(node.left, level + 1)] if node.left else []
            queue += [(node.right, level + 1)] if node.right else []
        level_sum_sorted = sorted(level_sum.values(), reverse = True)
        return level_sum_sorted[k - 1] if k <= len(level_sum_sorted) else -1


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.kthLargestLevelSum(deserializeTree("[5, 8, 9, 2, 1, 3, 7, 4, 6]"), 2), 13)

    def testcase2(self):
        self.assertEqual(self.soln_obj.kthLargestLevelSum(deserializeTree("[1, 2, null, 3]"), 1), 3)

    def testcase3(self):
        self.assertEqual(self.soln_obj.kthLargestLevelSum(deserializeTree("[5, 8, 9, 2, 1, 3, 7]"), 4), -1)

    def testcase4(self):
        self.assertEqual(self.soln_obj.kthLargestLevelSum(deserializeTree("[411310, 211244, 111674]"), 2), 322918)


if __name__ == '__main__':
    unittest.main()
