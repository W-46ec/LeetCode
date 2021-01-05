
"""
# Permutations II

Given a collection of numbers, `nums`, that might contain duplicates, return *all possible unique permutations **in any order***.


**Example 1:** 
```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

**Example 2:** 
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Constraints:** 
    - `1 <= nums.length <= 8` 
    - `-10 <= nums[i] <= 10` 
"""

from typing import List
from itertools import permutations
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # # Built-in method
        # return list(set(permutations(nums)))

        # Backtracking
        ans = []
        counter = Counter(nums)

        def solve(curr = []):
            if len(curr) == len(nums):
                ans.append(curr.copy())
            else:
                for x in counter:
                    if counter[x] > 0:
                        counter[x] -= 1
                        solve(curr + [x])
                        counter[x] += 1

        solve()
        return ans

# [(1, 2, 1), (2, 1, 1), (1, 1, 2)]
print(Solution().permuteUnique([1, 1, 2]))

# [(3, 1, 2), (1, 3, 2), (3, 2, 1), (2, 3, 1), (1, 2, 3), (2, 1, 3)]
print(Solution().permuteUnique([1, 2, 3]))

