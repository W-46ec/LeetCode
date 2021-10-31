
"""
# Count Nodes With the Highest Score

There is a **binary** tree rooted at `0` consisting of `n` nodes. The nodes are labeled from `0` to `n - 1`. You are given a **0-indexed** integer array `parents` representing the tree, where `parents[i]` is the parent of node `i`. Since node `0` is the root, `parents[0] == -1`.

Each node has a **score**. To find the score of a node, consider if the node and the edges connected to it were **removed**. The tree would become one or more **non-empty** subtrees. The **size** of a subtree is the number of the nodes in it. The **score** of the node is the **product of the sizes** of all those subtrees.

Return *the **number** of nodes that have the **highest score***.


**Example 1:** 
![2049_example-1](./img/2049_example-1.png)
```
Input: parents = [-1,2,0,2,0]
Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
```

**Example 2:** 
![2049_example-2](./img/2049_example-2.png)
```
Input: parents = [-1,2,0]
Output: 2
Explanation:
- The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
```

**Constraints:** 
    - `n == parents.length` 
    - `2 <= n <= 10^5` 
    - `parents[0] == -1` 
    - `0 <= parents[i] <= n - 1` for `i != 0` 
    - `parents` represents a valid binary tree.

**Hint 1** 
For each node, you need to find the sizes of the subtrees rooted in each of its children. Maybe DFS?

**Hint 2** 
How to determine the number of nodes in the rest of the tree? Can you subtract the size of the subtree rooted at the node from the total number of nodes of the tree?

**Hint 3** 
Use these values to compute the score of the node. Track the maximum score, and how many nodes achieve such score.
"""

from typing import List
from collections import defaultdict

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)
        for i in range(1, len(parents)):
            tree[parents[i]] += [i]
        
        sizes = {}
        def post_order(idx = 0):
            if idx not in tree:
                return (0, 0, len(parents) - 1)
            sizes[tree[idx][0]] = post_order(tree[idx][0])
            left_child_num = sizes[tree[idx][0]][0] + sizes[tree[idx][0]][1] + 1
            right_child_num = 0
            if len(tree[idx]) == 2:
                sizes[tree[idx][1]] = post_order(tree[idx][1])
                right_child_num = sizes[tree[idx][1]][0] + sizes[tree[idx][1]][1] + 1
            return (
                left_child_num, 
                right_child_num, 
                len(parents) - left_child_num - right_child_num - 1
            )
        
        sizes[0] = post_order()
        
        scores = [0] * len(parents)
        for node in sizes:
            total = 1
            for score in sizes[node]:
                if score > 0:
                    total *= score
            scores[node] = total
        
        return scores.count(max(scores))

# 3
print(Solution().countHighestScoreNodes([-1, 2, 0, 2, 0]))

# 2
print(Solution().countHighestScoreNodes([-1, 2, 0]))
