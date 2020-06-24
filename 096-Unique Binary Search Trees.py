
"""
# Unique Binary Search Trees

Given *n*, how many structurally unique **BST's** (binary search trees) that store values 1 ... *n*?

**Example:** 
```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```
"""

class Solution:
    def numTrees(self, n: int) -> int:
        Tn = [1]
        for i in range(n):
            c = 0
            for j in range(len(Tn)):
                c += Tn[j] * Tn[len(Tn) - j - 1]
            Tn += [c]
        return Tn[-1]

for i in range(10):
    print(Solution().numTrees(i))

