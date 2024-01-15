
"""
# Valid Sudoku

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:
    1. Each row must contain the digits `1-9` without repetition.
    2. Each column must contain the digits `1-9` without repetition.
    3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:** 
    - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    - Only the filled cells need to be validated according to the mentioned rules.


**Example 1:** 
![036_250px-Sudoku-by-L2G-20050714.svg](./img/036_250px-Sudoku-by-L2G-20050714.svg.png)
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:** 
```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Constraints:** 
    - `board.length == 9` 
    - `board[i].length == 9` 
    - `board[i][j]` is a digit `1-9` or `'.'`.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain the digits 1-9 without repetition
        for row in board:
            digits = list(filter(lambda x: x.isnumeric(), row))
            if len(set(digits)) != len(digits):
                return False
        
        # Each column must contain the digits 1-9 without repetition
        for col in zip(*board):
            digits = list(filter(lambda x: x.isnumeric(), col))
            if len(set(digits)) != len(digits):
                return False
        
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition
        subboxes = { i: set() for i in range(9) }
        for i in range(9):
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in subboxes[(i // 3) * 3 + (j // 3)]:
                        return False
                    subboxes[(i // 3) * 3 + (j // 3)].add(board[i][j])

        return True

# True
print(Solution().isValidSudoku([
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'], 
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'], 
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'], 
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'], 
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'], 
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'], 
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'], 
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'], 
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]))

# False
print(Solution().isValidSudoku([
    ['8', '3', '.', '.', '7', '.', '.', '.', '.'], 
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'], 
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'], 
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'], 
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'], 
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'], 
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'], 
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'], 
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]))

# True
print(Solution().isValidSudoku([
    ['.', '8', '7', '6', '5', '4', '3', '2', '1'], 
    ['2', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['3', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['4', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['5', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['6', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['7', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['8', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['9', '.', '.', '.', '.', '.', '.', '.', '.']
]))

# False
print(Solution().isValidSudoku([
    ['.', '.', '.', '.', '.', '.', '5', '.', '.'], 
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['9', '3', '.', '.', '2', '.', '4', '.', '.'], 
    ['.', '.', '7', '.', '.', '.', '3', '.', '.'], 
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['.', '.', '.', '3', '4', '.', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '3', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '5', '2', '.', '.']
]))