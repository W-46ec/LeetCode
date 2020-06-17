
"""
# Surrounded Regions

Given a 2D board containing `'X'` and `'O'` (**the letter O**), capture all regions surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example:** 
```
X X X X
X O O X
X X O X
X O X X
```

After running your function, the board should be:
```
X X X X
X X X X
X X X X
X O X X
```

**Explanation:** 
Surrounded regions shouldn’t be on the border, which means that any `'O'` on the border of the board are not flipped to `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be flipped to `'X'`. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        def bfs(grid, x, y, old, new):
            Q = [(x, y)]
            while Q:
                r, c = Q.pop(0)
                grid[r][c] = new
                if r > 0 and grid[r - 1][c] == old and (r - 1, c) not in Q:
                    Q.append((r - 1, c))
                if r < len(grid) - 1 and grid[r + 1][c] == old and (r + 1, c) not in Q:
                    Q.append((r + 1, c))
                if c > 0 and grid[r][c - 1] == old and (r, c - 1) not in Q:
                    Q.append((r, c - 1))
                if c < len(grid[r]) - 1 and grid[r][c + 1] == old and (r, c + 1) not in Q:
                    Q.append((r, c + 1))

        for i in range(len(board)):
            if board[i][0] == 'O':
                bfs(board, i, 0, 'O', 'B')
            if board[i][-1] == 'O':
                bfs(board, i, len(board[i]) - 1, 'O', 'B')
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                bfs(board, 0, j, 'O', 'B')
            if board[-1][j] == 'O':
                bfs(board, len(board) - 1, j, 'O', 'B')
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = 'O' if board[i][j] == 'B' else 'X'

board = [
    ['X', 'X', 'X', 'X'], 
    ['X', 'O', 'O', 'X'], 
    ['X', 'X', 'O', 'X'], 
    ['X', 'O', 'X', 'X']
]

for r in board:
    print("".join(r))
print()
Solution().solve(board)
print("===>")
for r in board:
    print("".join(r))
print()

board = [
    ['X', 'O', 'X', 'O', 'X', 'O'], 
    ['O', 'X', 'O', 'X', 'O', 'X'], 
    ['X', 'O', 'X', 'O', 'X', 'O'], 
    ['O', 'X', 'O', 'X', 'O', 'X']
]

for r in board:
    print("".join(r))
print()
Solution().solve(board)
print("===>")
for r in board:
    print("".join(r))
print()


board = [
    ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
    ['O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'], 
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'], 
    ['O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O'], 
    ['O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'], 
    ['X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'], 
    ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O'], 
    ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'O', 'O', 'O'], 
    ['O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O'], 
    ['X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X'], 
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'X'], 
    ['O', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O'], 
    ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
    ['O', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O'], 
    ['O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'O'], 
    ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'O'], 
    ['O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O'], 
    ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O'], 
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
    ['X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O']
]

for r in board:
    print("".join(r))
print()
Solution().solve(board)
print("===>")
for r in board:
    print("".join(r))
print()
