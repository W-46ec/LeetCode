
"""
# Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

**Example:** 
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```
"""

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

# Reference: https://leetcode.com/problems/path-sum-iii/discuss/779227/Python-dfs-%2B-hash-table-using-cumulative-sums-explained

import sys
sys.path.append('../')

from util import TreeNode, initTree
from collections import defaultdict

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        counter = defaultdict(int)
        # Special case: when cummulative_sum == sum, it should be counted
        counter[0] = 1

        def traverse(tree, counter, cummulative_sum = 0):
            if not tree:
                return 0
            cummulative_sum += tree.val
            ans = counter[cummulative_sum - sum]
            counter[cummulative_sum] += 1
            ans += traverse(tree.left, counter, cummulative_sum) + \
                traverse(tree.right, counter, cummulative_sum)
            counter[cummulative_sum] -= 1
            return ans

        return traverse(root, counter)

# # Testcases
# [10,5,-3,3,2,null,11,3,-2,null,1]
# 8
# [1,null,2,null,3,null,4,null,5]
# 3
# [1,-2,-3,1,3,-2,null,-1]
# 3

# 3
print(Solution().pathSum(initTree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))

# 2
print(Solution().pathSum(initTree([1, None, 2, None, 3, None, 4, None, 5]), 3))

# 1
print(Solution().pathSum(initTree([1, -2, -3, 1, 3, -2, None, -1]), 3))

