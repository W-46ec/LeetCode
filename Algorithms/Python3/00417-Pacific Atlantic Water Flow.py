
"""
# 417. Pacific Atlantic Water Flow

Given an `m x n` matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

**Note:** 
	1. The order of returned grid coordinates does not matter.
	2. Both *m* and *n* are less than 150.


**Example:** 
```
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
```
"""

from typing import List
from collections import defaultdict

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        # Indicate which cell is reachable by which ocean
        #    1: Reachable by the Pacific ocean
        #    2: Reachable by the Atlantic ocean
        #    3: Reachable by both
        reachable = defaultdict(int)
        
        def bfs(queue: List[tuple], ocean: int) -> None:
            visited = defaultdict(bool, { k: True for k in queue })
            while queue:
                x, y = queue.pop(0)
                reachable[(x, y)] += ocean
                for dx, dy in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                    if 0 <= x + dx < len(matrix) \
                            and 0 <= y + dy < len(matrix[0]) \
                            and not visited[(x + dx, y + dy)] \
                            and matrix[x + dx][y + dy] >= matrix[x][y]:
                        queue += [(x + dx, y + dy)]
                        visited[(x + dx, y + dy)] = True
        
        # Set up initial queues
        queue_Pac = [(i, 0) for i in range(len(matrix))] \
            + [(0, i) for i in range(1, len(matrix[0]))]
        queue_Atl = [(i, len(matrix[0]) - 1) for i in range(len(matrix))] \
            + [(len(matrix) - 1, i) for i in range(len(matrix[0]) - 1)]
        
        # Run bfs to expand reachable area of the Pacific ocean
        bfs(queue_Pac, 1)
        # Run bfs to expand reachable area of the Atlantic ocean
        bfs(queue_Atl, 2)
        
        return [[x, y] for x, y in reachable if reachable[(x, y)] == 3]

# [[3, 0], [4, 0], [0, 4], [3, 1], [1, 3], [2, 2], [1, 4]]
print(Solution().pacificAtlantic([
	[1, 2, 2, 3, 5], 
	[3, 2, 3, 4, 4], 
	[2, 4, 5, 3, 1], 
	[6, 7, 1, 4, 5], 
	[5, 1, 1, 2, 4]
]))

# []
print(Solution().pacificAtlantic([]))
