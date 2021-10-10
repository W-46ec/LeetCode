
"""
# Find Winner on a Tic Tac Toe Game

**Tic-tac-toe** is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:
    - Players take turns placing characters into empty squares `' '`.
    - The first player `A` always places `'X'` characters, while the second player `B` always places `'O'` characters.
    - `'X'` and `'O'` characters are always placed into empty squares, never on filled ones.
    - The game ends when there are **three** of the same (non-empty) character filling any row, column, or diagonal.
    - The game also ends if all squares are non-empty.
    - No more moves can be played if the game is over.

Given a 2D integer array `moves` where `moves[i] = [row_i, col_i]` indicates that the `ith` move will be played on `grid[row_i][col_i]`. return *the winner of the game if it exists* (`A` or `B`). In case the game ends in a draw return `"Draw"`. If there are still movements to play return `"Pending"`.

You can assume that `moves` is valid (i.e., it follows the rules of **Tic-Tac-Toe**), the grid is initially empty, and `A` will play first.


**Example 1:**
![1275_xo1-grid](./img/1275_xo1-grid.jpg)
```
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
```

**Example 2:** 
![1275_xo1-grid](./img/1275_xo2-grid.jpg)
```
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.
```

**Example 3:** 
![1275_xo1-grid](./img/1275_xo3-grid.jpg)
```
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
```

**Example 4:** 
![1275_xo1-grid](./img/1275_xo4-grid.jpg)
```
Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
```

**Constraints:** 
    - `1 <= moves.length <= 9` 
    - `moves[i].length == 2` 
    - `0 <= rowi, coli <= 2` 
    - There are no repeated elements on `moves`.
    - `moves` follow the rules of tic tac toe.

**Hint #1** 
It's straightforward to check if A or B won or not, check for each row/column/diag if all the three are the same.

**Hint #2** 
Then if no one wins, the game is a draw iff the board is full, i.e. moves.length = 9 otherwise is pending.
"""

from typing import List

class Solution:
    def checkWin(self, board: List[List[int]], player: int) -> bool:
        diagonal = [[0, 0], [1, 1], [2, 2]]
        anti_diagonal = [[2, 0], [1, 1], [0, 2]]
        if any(map(lambda x: x == player * 3, map(sum, board))):
            return True
        elif any(map(lambda x: x == player * 3, [sum(col) for col in zip(*board)])):
            return True
        elif sum([board[x][y] for x, y in diagonal]) == player * 3:
            return True
        elif sum([board[x][y] for x, y in anti_diagonal]) == player * 3:
            return True
        else:
            return False
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0] * 3 for _ in range(3)]
        player = 1      # 1 for player A; -1 for player B
        move_count = 0
        for x, y in moves:
            move_count += 1
            board[x][y] = player
            player *= -1
        if self.checkWin(board, 1):
            return "A"
        elif self.checkWin(board, -1):
            return "B"
        elif move_count == 9:
            return "Draw"
        else:
            return "Pending"

# "A"
print(Solution().tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))

# "B"
print(Solution().tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))

# "Draw"
print(Solution().tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))

# "Pending"
print(Solution().tictactoe([[0, 0], [1, 1]]))

