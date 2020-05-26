
"""
# Leftmost Column with at Least a One

*(This problem is an **interactive problem**.)*

A binary matrix means that all elements are `0` or `1`. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a `1` in it. If such index doesn't exist, return `-1`.

**You can't access the Binary Matrix directly.** You may only access the matrix using a `BinaryMatrix` interface:
    - `BinaryMatrix.get(row, col)` returns the element of the matrix at index `(row, col)` (0-indexed).
    - `BinaryMatrix.dimensions()` returns a list of 2 elements `[rows, cols]`, which means the matrix is `rows * cols`.

Submissions making more than `1000` calls to `BinaryMatrix.get` will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix `mat` as input in the following four examples. You will not have access the binary matrix directly.


Example 1:
![21_Example-1](./img/21_Example-1.png)

Input: mat = [[0,0],[1,1]]
Output: 0


Example 2:
![21_Example-2](./img/21_Example-2.png)

Input: mat = [[0,0],[0,1]]
Output: 1


Example 3:
![21_Example-3](./img/21_Example-3.png)

Input: mat = [[0,0],[0,0]]
Output: -1


Example 4:
![21_Example-4](./img/21_Example-4.png)

Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:
    - `rows == mat.length`
    - `cols == mat[i].length`
    - `1 <= rows, cols <= 100`
    - `mat[i][j]` is either `0` or `1`.
    - `mat[i]` is sorted in a non-decreasing way.
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def binarySearch(row, lo, hi):
            mid = (lo + hi) // 2
            l, r = binaryMatrix.get(row, lo), binaryMatrix.get(row, hi)
            if r <= 0:
                return -1
            if l >= 1:
                return lo
            m = binaryMatrix.get(row, mid)
            if m >= 1:
                return binarySearch(row, lo, mid)
            else:
                return binarySearch(row, mid + 1, hi)
        n, m = binaryMatrix.dimensions()
        ans = -1
        for row in range(n):
            if ans == -1:
                ans = binarySearch(row, 0, m - 1)
            else:
                if binaryMatrix.get(row, ans) == 1:
                    ans = binarySearch(row, 0, ans)
        return ans

