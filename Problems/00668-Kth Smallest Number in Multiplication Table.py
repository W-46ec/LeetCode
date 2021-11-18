
"""
# Kth Smallest Number in Multiplication Table

Nearly everyone has used the [Multiplication Table](https://en.wikipedia.org/wiki/Multiplication_table). The multiplication table of size `m x n` is an integer matrix `mat` where `mat[i][j] == i * j` (**1-indexed**).

Given three integers `m`, `n`, and `k`, return *the `kth` smallest element in the `m x n` multiplication table*.


**Example 1:** 
![668_multtable1-grid](./img/668_multtable1-grid.jpg)
```
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.
```

**Example 2:** 
![668_multtable2-grid](./img/668_multtable2-grid.jpg)
```
Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.
```

**Constraints:** 
    - `1 <= m, n <= 3 * 10^4` 
    - `1 <= k <= m * n` 
"""

# Reference: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/solution/

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            
            count = 0
            for i in range(1, m + 1):
                count += min(mid // i, n)
            
            if count < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

# 3
print(Solution().findKthNumber(3, 3, 5))

# 6
print(Solution().findKthNumber(2, 3, 6))
