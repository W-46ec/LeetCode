
"""
# Search a 2D Matrix

Write an efficient algorithm that searches for a value in an `m x n` matrix. This matrix has the following properties:
    - Integers in each row are sorted from left to right.
    - The first integer of each row is greater than the last integer of the previous row.


**Example 1:** 
![074_mat](./img/074_mat.jpg)
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
```

**Example 2:** 
![074_mat2](./img/074_mat2.jpg)
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
```

**Example 3:** 
```
Input: matrix = [], target = 0
Output: false
```

**Constraints:** 
    - `m == matrix.length` 
    - `n == matrix[i].length` 
    - `0 <= m, n <= 100` 
    - `-10^4 <= matrix[i][j], target <= 10^4` 
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:    
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            lo = mid + 1 if target > nums[mid] else lo
            hi = mid - 1 if target < nums[mid] else hi
        return lo

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Perform binary search on the whole matrix
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l <= r:
            middle = (l + r) // 2
            if matrix[middle // col][middle % col] > target:
                r = middle - 1
            elif matrix[middle // col][middle % col] < target:
                l = middle + 1
            else:
                return True
        return False
        
        # # Two binary searches
        # if not matrix or not matrix[0]:
        #     return False
        # indices = [r[0] for r in matrix]
        # pos = self.searchInsert(indices, target)
        # if pos < len(indices):
        #     if target >= indices[pos]:
        #         idx = self.searchInsert(matrix[pos], target)
        #         return idx < len(matrix[pos]) and target == matrix[pos][idx]
        #     elif target < indices[pos] and pos > 0:
        #         idx = self.searchInsert(matrix[pos - 1], target)
        #         return idx < len(matrix[pos - 1]) and target == matrix[pos - 1][idx]
        #     else:
        #         return False
        # else:
        #     idx = self.searchInsert(matrix[-1], target)
        #     return idx < len(matrix[-1]) and target == matrix[-1][idx]

# True
print(Solution().searchMatrix([
    [1, 3, 5, 7], 
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 3))

# True
print(Solution().searchMatrix([
    [1, 3, 5, 7], 
    [10, 11, 16, 20], 
    [23, 30, 34, 50]
], 3))

# False
print(Solution().searchMatrix([], 0))

# False
print(Solution().searchMatrix([], 1))

# True
print(Solution().searchMatrix([[1, 3]], 3))

# False
print(Solution().searchMatrix([[1]], 2))

