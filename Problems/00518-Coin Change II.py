
"""
# Coin Change II

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the number of combinations that make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The answer is **guaranteed** to fit into a signed **32-bit** integer.


**Example 1:** 
```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2:** 
```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3:** 
```
Input: amount = 10, coins = [10]
Output: 1
```

**Constraints:** 
    - `1 <= coins.length <= 300` 
    - `1 <= coins[i] <= 5000` 
    - All the values of `coins` are **unique**.
    - `0 <= amount <= 5000` 
"""

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] <- number of ways to make up i using all coins
        dp = [0] * (amount + 1)

        # Base case: dp[0] is 1
        # When amount is 0, there is only 1 way to make up that amount -- not choosing any coins
        dp[0] = 1

        # For an arbitrary amount m, if the denomination of the last coin in the combination is d, 
        # then dp[m] is equal to 1 * dp[m - d] + dp[m].
        # Note: 1 + 2 + 2 = 5 and 2 + 1 + 2 = 5 are treated as the same combination.
        # To avoid overcounting, we should iterate through coins first.
        for d in coins:
            for m in range(d, amount + 1):
                dp[m] += dp[m - d]

        return dp[amount]

print(Solution().change(5, [1, 2, 5]))
print(Solution().change(3, [2]))
print(Solution().change(10, [10]))

