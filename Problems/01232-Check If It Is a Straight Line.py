
"""
# Check If It Is a Straight Line

You are given an array `coordinates`, `coordinates[i] = [x, y]`, where `[x, y]` represents the coordinate of a point. Check if these points make a straight line in the XY plane.


**Example 1:** 
![1232_untitled-diagram-2](./img/1232_untitled-diagram-2.jpg)
```
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
```

**Example 2:** 
![1232_untitled-diagram-1](./img/1232_untitled-diagram-1.jpg)
```
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
```

**Constraints:** 
    - `2 <= coordinates.length <= 1000` 
    - `coordinates[i].length == 2` 
    - `-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4` 
    - `coordinates` contains no duplicate point.
"""

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Proof:
        # ax1 + by1 + c = 0
        # ax2 + by2 + c = 0
        # => [a b] * [(x1 - x2) (y1 - y2)]^T = 0
        # Let b = (x1 - x2), then a = -(y1 - y2) = (y2 - y1)
        # => c = -(ax1 + by1)
        # All points in `coordinates` are on the same line iff axi + byi + c is 0.

        [x1, y1], [x2, y2] = coordinates[0], coordinates[1]
        a, b = y2 - y1, x1 - x2
        c = -(a * x1 + b * y1)
        return all([a * xi + b * yi == -c for xi, yi in coordinates])

print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))   # True
print(Solution().checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))   # False
print(Solution().checkStraightLine([[0, 0], [0, 1], [0, 2]]))   # True
print(Solution().checkStraightLine([[0, 1], [1, 1], [2, 1]]))   # True

