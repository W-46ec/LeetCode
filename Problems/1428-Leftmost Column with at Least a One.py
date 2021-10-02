
"""
# Leftmost Column with at Least a One

(*This problem is an **interactive problem***.)

A **row-sorted binary matrix** means that all elements are `0` or `1` and each row of the matrix is sorted in non-decreasing order.

Given a **row-sorted binary matrix** `binaryMatrix`, return *the index (0-indexed) of the **leftmost column** with a 1 in it*. If such an index does not exist, return `-1`.

**You can't access the Binary Matrix directly**. You may only access the matrix using a `BinaryMatrix` interface:

    - `BinaryMatrix.get(row, col)` returns the element of the matrix at index `(row, col)` (0-indexed).
    - `BinaryMatrix.dimensions()` returns the dimensions of the matrix as a list of 2 elements `[rows, cols]`, which means the matrix is `rows x cols`.

Submissions making more than `1000` calls to `BinaryMatrix.get` will be judged *Wrong Answer*. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.


**Example 1:** 

```
Input: mat = [[0,0],[1,1]]
Output: 0
```

**Example 2:** 

```
Input: mat = [[0,0],[0,1]]
Output: 1
```

**Example 3:** 

```
Input: mat = [[0,0],[0,0]]
Output: -1
```

**Example 4:** 

```
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
```

**Constraints:** 
    - `rows == mat.length` 
    - `cols == mat[i].length` 
    - `1 <= rows, cols <= 100` 
    - `mat[i][j]` is either `0` or `1`.
    - `mat[i]` is sorted in non-decreasing order.
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
