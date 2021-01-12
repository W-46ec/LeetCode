
"""
# Beautiful Arrangement

Suppose you have `n` integers labeled `1` through `n`. A permutation of those `n` integers `perm` (**1-indexed**) is considered a **beautiful arrangement** if for every `i` (`1 <= i <= n`), **either** of the following is true:
    - `perm[i]` is divisible by `i`.
    - `i` is divisible by `perm[i]`.

Given an integer `n`, return *the **number** of the **beautiful arrangements** that you can construct*.


**Example 1:** 
```
Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
```

**Example 2:** 
```
Input: n = 1
Output: 1
```

**Constraints:** 
    - `1 <= n <= 15` 
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        def solve(num_set, pos = 1):
            if not num_set:
                self.ans += 1
            else:
                for x in num_set:
                    if x % pos == 0 or pos % x == 0:
                        solve(num_set - {x}, pos + 1)
        solve(set(i for i in range(1, n + 1)))
        return self.ans

print(Solution().countArrangement(1))   # 1
print(Solution().countArrangement(2))   # 2
print(Solution().countArrangement(3))   # 3
print(Solution().countArrangement(4))   # 8
print(Solution().countArrangement(5))   # 10

