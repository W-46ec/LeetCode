
"""
# K-th Symbol in Grammar

We build a table of `n` rows (**1-indexed**). We start by writing `0` in the `1st` row. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

- For example, for `n = 3`, the `1st` row is `0`, the `2nd` row is `01`, and the `3rd` row is `0110`.

Given two integer `n` and `k`, return the `kth` (**1-indexed**) symbol in the `nth` row of a table of `n` rows.


**Example 1:** 
```
Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
```

**Example 2:** 
```
Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01
```

**Example 3:** 
```
Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01
```

**Constraints:** 
    - `1 <= n <= 30` 
    - `1 <= k <= 2^(n - 1)` 
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        The table is given by the following:
        row 1: 0
        row 2: 01
        row 3: 0110
        row 4: 01101001
        row 5: 0110100110010110
        ...

        As we can see, for an arbitrary row i (i >= 2), the length 
        of row i is 2 times the length of row (i - 1).
        The first half of row i is exactly the same as row (i - 1), 
        and the second half of row i is the negation of row (i - 1).

        Therefore, if k is in the first half of row i, it is equivalent
        to query the kth symbol in row (i - 1).
        If k is in the second half if row i, it is equivalent to query 
        the negation of the kth symbol in row (i - 1).
        We may repeat the above steps recursively until we reduce k to 1.
        Simply count the number of negation operations.
        """
        negate = 0
        for x in range(n - 1, -1, -1):
            # Length of row (i - 1)
            row_len = 1 << x
            # k is in the second half of row i
            if k > row_len:
                # Take negation
                negate = (negate + 1) % 2
                # Minus k by 2^row_len
                k &= (-1 ^ row_len)
        return int(negate)

# 0
print(Solution().kthGrammar(1, 1))

# 0
print(Solution().kthGrammar(2, 1))

# 1
print(Solution().kthGrammar(2, 2))

# 0
print(Solution().kthGrammar(30, 434991989))
