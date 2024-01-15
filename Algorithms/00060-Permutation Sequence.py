
"""
# Permutation Sequence

The set `[1,2,3,...,n]` contains a total of *n*! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for *n* = 3:
    1. `"123"` 
    2. `"132"` 
    3. `"213"` 
    4. `"231"` 
    5. `"312"` 
    6. `"321"` 

Given *n* and *k*, return the kth permutation sequence.

**Note:** 
    Given *n* will be between 1 and 9 inclusive.
    Given *k* will be between 1 and *n*! inclusive.

**Example 1:** 
```
Input: n = 3, k = 3
Output: "213"
```

**Example 2:** 
```
Input: n = 4, k = 9
Output: "2314"
```
"""

from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = "123456789"
        p = permutations(s[ : n], n)
        i = 1
        while i < k:
            next(p)
            i += 1
        return "".join(next(p))

print(Solution().getPermutation(3, 3))      # "213"
print(Solution().getPermutation(4, 9))      # "2314"
                
