
"""
# Combinations

Given two integers `n` and `k`, return *all possible combinations of `k` numbers chosen from the range `[1, n]`*.

You may return the answer in **any order**.


**Example 1:** 
```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
```

**Example 2:** 
```
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
```

**Constraints:** 
    - `1 <= n <= 20` 
    - `1 <= k <= n` 
"""

from typing import List
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # Built-in function
        # return combinations(range(1, n + 1), k)

        # Resursive approach
        def _combinations(start, end, k):
            if k == 1:
                return [[x] for x in range(start, end + 1)]
            res_comb = []
            for x in range(start, end - k + 2):
                sub_comb = _combinations(x + 1, end, k - 1)
                res_comb += [[x] + lst for lst in sub_comb]
            return res_comb
        return _combinations(1, n, k)


# [[1], [2], [3], [4]]
print(Solution().combine(4, 1))

# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(Solution().combine(4, 2))

# [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
print(Solution().combine(4, 3))

# [[1, 2, 3, 4]]
print(Solution().combine(4, 4))

# [[1]]
print(Solution().combine(1, 1))
