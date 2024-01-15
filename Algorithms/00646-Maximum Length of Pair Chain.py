
"""
# Maximum Length of Pair Chain

You are given an array of `n` pairs `pairs` where `pairs[i] = [left_i, right_i]` and `left_i < right_i`.

A pair `p2 = [c, d]` **follows** a pair `p1 = [a, b]` if `b < c`. A **chain** of pairs can be formed in this fashion.

Return *the length longest chain which can be formed*.

You do not need to use up all the given intervals. You can select pairs in any order.


**Example 1:** 
```
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
```

**Example 2:** 
```
Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
```

**Constraints:** 
    - `n == pairs.length` 
    - `1 <= n <= 1000` 
    - `-1000 <= left_i < right_i <= 1000` 
"""

from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort all pairs in increasing order
        pairs = sorted(pairs)

        # dp[i] <- optimal solution for the first i pairs (i = 0, 1, 2, ..., n)
        # dp[0] <- 0
        dp = [0] * (len(pairs) + 1)

        # For the ith pair P, find the last pair in paris[ : i] (namely P') 
        # such that P' and P can form a chain. Assume the index for P' is j.
        # Then we have dp[i + 1] = max(dp[i + 1], dp[j + 1] + 1).
        # Note: the ith pair is corresponding to dp[i + 1].
        longest_chain_len = 0
        for i, (l, r) in enumerate(pairs):
            j = i
            while j >= 0 and l <= pairs[j][1]:
                j -= 1
            dp[i + 1] = max(dp[i + 1], dp[j + 1] + 1)
            longest_chain_len = max(longest_chain_len, dp[i + 1])
        return longest_chain_len

# 2
print(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]))

# 3
print(Solution().findLongestChain([[1, 2], [7, 8], [4, 5]]))
