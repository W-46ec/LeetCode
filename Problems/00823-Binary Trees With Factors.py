
"""
# Binary Trees With Factors

Given an array of unique integers, `arr`, where each integer `arr[i]` is strictly greater than `1`.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return *the number of binary trees we can make*. The answer may be too large so return the answer **modulo** `10^9 + 7`.


**Example 1:** 
```
Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
```

**Example 2:** 
```
Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
```

**Constraints:** 
    - `1 <= arr.length <= 1000` 
    - `2 <= arr[i] <= 10^9` 
"""

from typing import List
from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Dynamic programming approach
        Let dp[k] be the total number of trees that are rooted at k (i.e., we
        can form dp[k] different trees with root value equal to k). And k is in arr.

        For any pair of factors (p, q), where p * q is k and p, q are in arr,
        we can form dp[p] * dp[q] trees with root value equal to k.
        Therefore, we have the following equation:

        dp[k] = sum(dp[p] * dp[q] for all p, q in arr such that p * q == k)

        Eventually, sum up the value of dp[k] for all k in arr will give us the answer.
        """

        # Sort the integers so that we can start with the smallest numbers first
        arr = sorted(arr)
        # Initialization -- each integer can form one tree by itself
        dp = defaultdict(int, { x: 1 for x in arr })

        # Build the solution bottom-up
        for i in range(len(arr)):
            # Check through arr[ : i] to find all factors of arr[i]
            for j in range(i):
                # If arr[j] divides arr[i], add the number of trees that form arr[j] times
                # the number of trees that form arr[arr[i] // arr[j]] to dp[arr[i]].
                q = arr[i] // arr[j]
                dp[arr[i]] += dp[q] * dp[arr[j]] if q * arr[j] == arr[i] else 0

        return sum(dp.values()) % (10 ** 9 + 7)

# 3
print(Solution().numFactoredBinaryTrees([2, 4]))

# 7
print(Solution().numFactoredBinaryTrees([2, 4, 5, 10]))

