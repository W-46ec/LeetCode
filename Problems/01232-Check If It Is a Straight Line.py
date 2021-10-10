
"""
# Check If It Is a Straight Line

You are given an array `coordinates`, `coordinates[i] = [x, y]`, where `[x, y]` represents the coordinate of a point. Check if these points make a straight line in the XY plane.


Example 1:

```
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
```

Example 2:

```
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
```

Constraints:
    - `2 <= coordinates.length <= 1000` 
    - `coordinates[i].length == 2` 
    - `-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4` 
    - `coordinates` contains no duplicate point.
"""

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        x1, y1 = coordinates[0]         # Point 1
        x2, y2 = coordinates[1]         # Point 2
        n1, n2 = y1 - y2, x2 - x1       # Norm Vector
        t = n1 * x1 + n2 * y1           # 2D hyperplane: H_{(x_2 - x_1, y_2 - y_1)}^t
        for ptr in coordinates[2 : ]:   # Check if other points are on the same line
            # (x, y) \cdot \vec{n} == t
            if ptr[0] * n1 + ptr[1] * n2 != t:
                return False
        return True

print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))   # True
print(Solution().checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))   # False
print(Solution().checkStraightLine([[0, 0], [0, 1], [0, 2]]))   # True
print(Solution().checkStraightLine([[0, 1], [1, 1], [2, 1]]))   # True

