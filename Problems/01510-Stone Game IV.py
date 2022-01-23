
"""
# Stone Game IV

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `n` stones in a pile. On each player's turn, that player makes a move consisting of removing **any** non-zero **square number** of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer `n`. Return `True` if and only if Alice wins the game otherwise return `False`, assuming both players play optimally.


**Example 1:** 
```
Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
```

**Example 2:** 
```
Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
```

**Example 3:** 
```
Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
```

**Example 4:** 
```
Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0). 
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).
```

**Example 5:** 
```
Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
```

**Constraints:** 
    - `1 <= n <= 10^5` 

**Hint #1** 
Use dynamic programming to keep track of winning and losing states. Given some number of stones, Alice can win if she can force Bob onto a losing state.
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Define a square number generator
        # i.e., 1, 4, 9, 16, ...
        def sqr_num():
            i = 1
            while True:
                yield i ** 2
                i += 1
        
        # dp[i] <- Whether or not Alice has a winning strategy
        #          if she starts with i stones
        # i = 1, 2, 3, ..., n
        dp = [True] * (n + 1)
        
        # Build the solution bottom-up
        for i in range(2, n + 1):
            # The set of all possible moves
            sqr_num_gen = sqr_num()
            
            # Get the set of all legal moves, starting from 1
            legal_move = next(sqr_num_gen)
            # Whether or not Alice has winning strategy
            has_win_strategy = False
            # Try all possible moves to find one that
            # results in a wining state.
            while legal_move <= i:
                # If i is a square number, Alice wins
                if legal_move == i:
                    has_win_strategy = True
                # To win the game, we need to take a square number 
                # of stones (i.e., legal_move stomes) away such that
                # the remaining number of stones will lead to a
                # losing state (i.e., dp[i - legal_move] is False).
                # That way, we are forcing our opponent (i.e., Bob)
                # into a losing state.
                elif dp[i - legal_move] == False:
                    has_win_strategy = True
                    break
                legal_move = next(sqr_num_gen)
            dp[i] = has_win_strategy
        
        # Solution
        return dp[n]


print(Solution().winnerSquareGame(1))   # True
print(Solution().winnerSquareGame(2))   # False
print(Solution().winnerSquareGame(4))   # True
print(Solution().winnerSquareGame(7))   # False
print(Solution().winnerSquareGame(17))  # False

