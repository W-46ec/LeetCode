
"""
# Rectangle Overlap

An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is **positive**. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return *`true` if they overlap, otherwise return `false`*.


**Example 1:** 
```
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
```

**Example 2:** 
```
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
```

**Example 3:** 
```
Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
```

**Constraints:** 
    - `rec1.length == 4` 
    - `rec2.length == 4` 
    - `-10^9 <= rec1[i], rec2[i] <= 10^9` 
    - `rec1` and `rec2` represent a valid rectangle with a non-zero area.
"""

from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Instead of thinking about overlapping, think about the cases where the two
        # rectangles are not overlapping. And then take the negation of them.
        bx1, by1, tx1, ty1 = rec1
        bx2, by2, tx2, ty2 = rec2
        return not ((bx2 - bx1 >= tx1 - bx1) \
            or (bx1 - bx2 >= tx2 - bx2) \
            or (by2 - by1 >= ty1 - by1) \
            or (by1 - by2 >= ty2 - by2))

# True
print(Solution().isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))

# False
print(Solution().isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))

# False
print(Solution().isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]))

# True
print(Solution().isRectangleOverlap([7, 8, 13, 15], [10, 8, 12, 20]))
