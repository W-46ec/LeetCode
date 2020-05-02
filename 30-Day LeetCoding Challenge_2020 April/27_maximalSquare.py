
"""
# Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def explore(matrix, i, j):
            row, col = len(matrix), len(matrix[0])
            i2, j2 = i, j
            while i2 < row and j2 < col and matrix[i2][j2] == '1':
                if all([matrix[x][j2] == '1' for x in range(i, i2 + 1)]) and \
                    all([matrix[i2][y] == '1' for y in range(j, j2 + 1)]):
                    i2 += 1
                    j2 += 1
                else:
                    break
            # print(i, j, i2, j2)
            return (i2 - 1, j2 - 1)

        if len(matrix) <= 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        maxR, maxC, maxLen = 0, 0, 0
        i = 0
        while i < row:
            j = 0
            while j < col:
                if matrix[i][j] == '1':
                    i2, j2 = explore(matrix, i, j)
                    if i2 != -1:
                        maxLen = max(maxLen, i2 - i + 1)
                j += 1
            i += 1
        return maxLen ** 2


print(Solution().maximalSquare([]))

print(Solution().maximalSquare([
    ['1', '0', '1', '0', '0'], 
    ['1', '0', '1', '1', '1'], 
    ['1', '1', '1', '1', '1'], 
    ['1', '0', '0', '1', '0']
]))

print(Solution().maximalSquare([
    ['1']
]))

print(Solution().maximalSquare([
    ['0']
]))

print(Solution().maximalSquare([
    ['1', '0', '1', '1', '1', '0', '0', '0', '1', '0'], 
    ['0', '1', '0', '0', '0', '0', '0', '1', '1', '0'], 
    ['0', '1', '0', '1', '0', '0', '0', '0', '1', '1'], 
    ['1', '1', '1', '0', '0', '0', '0', '0', '1', '0'], 
    ['0', '1', '1', '1', '0', '0', '1', '0', '1', '0'], 
    ['1', '1', '0', '1', '1', '0', '1', '1', '1', '0']
]))

print(Solution().maximalSquare([
    ['0', '0', '0', '1'], 
    ['1', '1', '0', '1'], 
    ['1', '1', '1', '1'], 
    ['0', '1', '1', '1'], 
    ['0', '1', '1', '1']
]))
