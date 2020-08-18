
"""
# Numbers With Same Consecutive Differences

Return all non-negative integers of length `N` such that the absolute difference between every two consecutive digits is `K`.

Note that **every** number in the answer **must not** have leading zeros **except** for the number `0` itself. For example, `01` has one leading zero and is invalid, but `0` is valid.

You may return the answer in any order.


**Example 1:** 
```
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
```

**Example 2:** 
```
Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

**Note:** 
    1. `1 <= N <= 9` 
    2. `0 <= K <= 9` 
"""

from typing import List

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = [i for i in range(10)]
        for exp in range(N - 1):
            lst = []
            for i in range(len(ans)):
                last_digit, lo, hi = ans[i] % 10, 10 ** (exp + 1), 10 ** (exp + 2)
                if last_digit - K in range(10):
                    num = ans[i] * 10 + last_digit - K
                    lst += [num] if lo <= num and num < hi else []
                if last_digit + K in range(10) and K != 0:
                    num = ans[i] * 10 + last_digit + K
                    lst += [num] if lo <= num and num < hi else []
            ans = lst
        return ans

print(Solution().numsSameConsecDiff(3, 7))  # [181, 292, 707, 818, 929]
print(Solution().numsSameConsecDiff(2, 1))  # [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
print(Solution().numsSameConsecDiff(2, 0))  # [11, 22, 33, 44, 55, 66, 77, 88, 99]

