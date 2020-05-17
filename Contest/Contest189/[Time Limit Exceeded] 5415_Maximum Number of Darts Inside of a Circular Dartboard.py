
"""
# Maximum Number of Darts Inside of a Circular Dartboard

You have a very large square wall and a circular dartboard placed on the wall. You have been challenged to throw darts into the board blindfolded. Darts thrown at the wall are represented as an array of `points` on a 2D plane. 

Return the maximum number of points that are within or lie on **any** circular dartboard of radius `r`.


**Example 1:** 
![5415_sample_1_1806](./img/5415_sample_1_1806.png)
```
Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
```

**Example 2:** 
![5415_sample_2_1806](./img/5415_sample_2_1806.png)
```
Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
```

**Example 3:** 
```
Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
Output: 1
```

**Example 4:** 
```
Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
Output: 4
```

**Constraints:** 
    - `1 <= points.length <= 100` 
    - `points[i].length == 2` 
    - `-10^4 <= points[i][0], points[i][1] <= 10^4` 
    - `1 <= r <= 5000` 
"""

from typing import List
from math import sqrt

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def dist(p1, p2):
            return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        def colinear(coordinates):
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

        def findCenter(ptr1, ptr2, ptr3):
            mid1 = [0.5 * (ptr1[0] + ptr2[0]), 0.5 * (ptr1[1] + ptr2[1])]
            mid2 = [0.5 * (ptr1[0] + ptr3[0]), 0.5 * (ptr1[1] + ptr3[1])]
            direction1 = [ptr2[1] - ptr1[1], ptr1[0] - ptr2[0]]
            direction2 = [ptr3[1] - ptr1[1], ptr1[0] - ptr3[0]]

            # Find inverse matrix
            det = direction1[0] * (-direction2[1]) - (-direction2[0]) * direction1[1]

            s = (-direction2[1] * (mid2[0] - mid1[0]) + direction2[0] * (mid2[1] - mid1[1])) / det
            # t = (direction1[1] * (mid2[0] - mid1[0]) + direction1[0] * (mid2[1] - mid1[1])) / det

            return [s * direction1[0] + mid1[0], s * direction1[1] + mid1[1]]

        def countNum(center, points, r):
            count = 0
            for p in points:
                if dist(center, p) <= r:
                    count += 1
            return count

        ans = 1
        if len(points) <= 1:
            return 1
        elif len(points) == 2:
            return 2 if dist(points[0], points[1]) <= 2 * r else 1

        for i in range(len(points)):
            if ans >= len(points):
                break
            for j in range(i + 1, len(points)):
                if dist(points[i], points[j]) <= 2 * r:
                    ans = max(ans, 2)
                    center = [0.5 * (points[j][0] + points[i][0]), 0.5 * (points[j][1] + points[i][1])]
                    ans = max(ans, countNum(center, points, r))
                for k in range(j + 1, len(points)):
                    ptr1, ptr2, ptr3 = points[i], points[j], points[k]
                    if not colinear([ptr1, ptr2, ptr3]):
                        center = findCenter(ptr1, ptr2, ptr3)
                        if dist(center, ptr1) <= r:
                            ans = max(ans, countNum(center, points, r))
        return ans

print(Solution().numPoints([[-2, 0], [2, 0], [0, 2], [0, -2]], 2))                  # 4
print(Solution().numPoints([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], 5))   # 5
print(Solution().numPoints([[-2, 0], [2, 0], [0, 2], [0, -2]], 1))                  # 1
print(Solution().numPoints([[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]], 2))   # 4
print(Solution().numPoints([[4, 5], [-4, 1], [-3, 2], [-4, 0], [0, 2]], 5))         # 5

# 23
print(Solution().numPoints([[6596, -1720], [37, -1237], [2243, 1289], [6499, 1860], [-9932, -307], [-740, 7499], [7139, 232], [4748, -623], [7448, -9396], [-6738, -5464], [-7338, 5717], [-7773, -9791], [906, 8441], [-7250, -1932], [-6035, -4705], [-7319, -4499], [-4363, -806], [6572, 2055], [312, -6791], [-5288, 9215], [3897, 1546], [-5402, 7559], [1806, -892], [7306, -1581], [-1644, 8544], [-9907, -9400], [9825, -5920], [5984, -8576], [4398, 7423], [2264, -7300], [-1143, -5084], [-8524, -9409], [8321, -1752], [168, 9691], [3161, -6205], [8206, -9002], [-2982, -241], [7067, -3743], [-3032, -9940], [-6558, 1527], [-4276, 1034], [-714, 7003], [-3461, 5580], [1165, 112], [-3802, -3650], [-9756, -4006], [-7890, -1356], [-6671, 9159], [-1395, -4835], [9172, -5083], [5600, -8131], [-1235, 6549], [7631, -2481], [8910, 3914], [-2836, -1792], [-6256, 9600], [4034, 4502], [-1543, 5934], [6195, 2294], [-148, 7633], [-8855, 7000], [1310, -1715], [1291, -2927], [6712, 2151], [-6932, 4832], [4780, 7065], [-648, -6109], [2639, 506], [7916, -9521], [-2591, 3575], [8015, 7559], [589, -4130], [-6927, 5167], [5306, 1944], [-1796, 2463], [-583, 1534], [278, -4239], [-2055, 332], [-3678, 2510], [-6248, 6121], [5984, 9979], [4531, -4380], [5147, 8960], [-8223, -8222], [-193, -5365], [9564, 4708], [-9944, 8781], [7892, 1721], [688, -8216], [6988, 4908], [1435, 4774], [6136, 4612], [4193, -1752], [4416, 3460], [-7738, -4820]], 4196))

# 47
print(Solution().numPoints([[-19, -10], [-41, -13], [-48, 11], [-38, 21], [10, 11], [26, -5], [27, -10], [39, -20], [6, -31], [-24, -32], [-38, -29], [5, -25], [25, 12], [37, -13], [-1, 28], [19, -7], [9, -15], [-14, 9], [-46, -23], [11, -43], [-13, 10], [-23, -45], [11, -19], [49, 8], [-3, 40], [-28, 5], [37, -47], [-11, -36], [-28, 36], [-32, 25], [9, 28], [44, 5], [40, 19], [-14, -3], [-40, 45], [30, -34], [-31, 42], [40, 38], [-10, -22], [-23, 6], [-48, -46], [-6, -8], [47, -40], [-41, 31], [-30, -14], [27, -49], [-35, -12], [42, 18], [-15, -7], [-45, 22], [47, 4], [-5, 41], [-7, -9], [-29, 37], [-24, 46], [20, 23], [-45, 40], [-31, -7], [-27, 48], [19, 16], [-28, -19], [6, -42], [18, -33], [30, 50], [46, 29]], 47))


