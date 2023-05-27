
"""
# Stone Game II

Alice and Bob continue their games with piles of stones. There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first. Initially, `M = 1`.

On each player's turn, that player can take **all the stones** in the **first** `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.


**Example 1:** 
```
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
```

**Example 2:** 
```
Input: piles = [1,2,3,4,5,100]
Output: 104
```

**Constraints:** 
    - `1 <= piles.length <= 100` 
    - `1 <= piles[i] <= 10^4` 
"""

from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # soln[idx][M] <- the max score Alice can get if she starts 
        # from idx (i.e., piles[idx : ]) with value M
        soln = [[None] * (len(piles) + 1) for _ in range(len(piles))]

        # When Alice took the first x piles of stones, Bob will need to continue with 
        # the remaining (n - x) piles with a new M' = max(M, x).
        # And the max score Alice can get after taking x piles is the sum of all piles 
        # minus the max score Bob can get in the remaining (n - x) piles.
        # What Bob has to deal with in the next step is essentially the same problem 
        # except that the problem size is smaller.
        # Therefore we can solve it recursively.

        def solve(idx = 0, M = 1):
            # Base case: return 0 if all stones are taken.
            if idx >= len(piles):
                return 0
            # The sum of all piles in the current round of game.
            pile_sum = sum(piles[idx : ])
            if soln[idx][M] is None:
                max_score = float('-inf')
                # Try all possible x from 1 to 2M and choose the 
                # strategy that yield the max score.
                for x in range(1, 1 + min(2 * M, len(piles) - idx)):
                    max_score = max(max_score, pile_sum - solve(idx + x, max(M, x)))
                # Record the results to avoid repeated calculation.
                soln[idx][M] = max_score
            return soln[idx][M]

        return solve()

# 10
print(Solution().stoneGameII([2, 7, 9, 4, 4]))

# 104
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]))

# 3
print(Solution().stoneGameII([3]))

# 217
print(Solution().stoneGameII([77, 12, 64, 35, 28, 4, 87, 21, 20]))

# 98008
print(Solution().stoneGameII([8270, 7145, 575, 5156, 5126, 2905, 8793, 7817, 5532, 5726, 7071, 7730, 5200, 5369, 5763, 7148, 8287, 9449, 7567, 4850, 1385, 2135, 1737, 9511, 8065, 7063, 8023, 7729, 7084, 8407]))
