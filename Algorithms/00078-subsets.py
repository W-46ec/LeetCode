
"""
# Subsets

Given a set of **distinct** integers, *nums*, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:** 
```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```
"""

from typing import List
from itertools import combinations
from functools import reduce

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda x, y: x + y, [[list(x) for x in list(combinations(nums, i))] for i in range(len(nums) + 1)])

print(Solution().subsets([1, 2, 3]))

