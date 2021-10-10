
"""
# Transform to Chessboard

You are given an `n x n` binary grid `board`. In each move, you can swap any two rows with each other, or any two columns with each other.

Return *the minimum number of moves to transform the board into a **chessboard board***. If the task is impossible, return `-1`.

A **chessboard board** is a board where no `0`'s and no `1`'s are 4-directionally adjacent.


**Example 1:** 
![782_chessboard1-grid](./img/782_chessboard1-grid.jpg)
```
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.
```

**Example 2:** 
![782_chessboard2-grid](./img/782_chessboard2-grid.jpg)
```
Input: board = [[0,1],[1,0]]
Output: 0
Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
```

**Example 3:** 
![782_chessboard3-grid](./img/782_chessboard3-grid.jpg)
```
Input: board = [[1,0],[1,0]]
Output: -1
Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.
```

**Constraints:** 
    - `n == board.length` 
    - `n == board[i].length` 
    - `2 <= n <= 30` 
    - `board[i][j]` is either `0` or `1`.
"""

# Reference: https://leetcode.com/problems/transform-to-chessboard/solution/
# Reference: https://leetcode.com/problems/transform-to-chessboard/discuss/114843/Key-Observation-on-property-of-ChessBoard

from typing import List
from collections import Counter

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        length, ans = len(board), 0

        rows, cols = Counter(map(tuple, board)), Counter(zip(*board))

        # 1. There should be two kinds of lines
        # 2. When the length is even:
        #     The number of 1's should be the same as the number of 0's
        # 3. When the length is odd:
        #     There should be exactly one extra 0 or 1
        for ctr in [rows, cols]:
            if len(ctr) != 2 \
                    or sorted(ctr.values()) != [length // 2, (length + 1) // 2]:
                return -1

            # Each row/col should either be identical to
            # the first one or be the reverse of it
            line1, line2 = ctr.keys()
            if not all(x ^ y for x, y in zip(line1, line2)):
                return -1

            # When the length is even:
            #     It could either start with a 0 or 1
            # When the length is odd:
            #     It could only start with the more frequent number
            start = [Counter(line1).most_common()[0][0]] if length % 2 == 1 else [0, 1]

            # To transform line1 into the ideal line [i % 2 for i ...], 
            # we take the number of differences and divide by two
            ans += min(sum((i - x) % 2 for i, x in enumerate(line1, start)) for start in start) // 2
        
        return ans

# 2
print(Solution().movesToChessboard([
    [0, 1, 1, 0], 
    [0, 1, 1, 0], 
    [1, 0, 0, 1], 
    [1, 0, 0, 1]
]))

# 0
print(Solution().movesToChessboard([
    [0, 1], 
    [1, 0]
]))

# -1
print(Solution().movesToChessboard([
    [1, 0], 
    [1, 0]
]))
