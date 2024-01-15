
"""
# Min Cost to Connect All Points

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return *the minimum cost to make all points connected*. All points are connected if there is **exactly one** simple path between any two points.


**Example 1:** 
![1584_d](./img/1584_d.png)
```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
![1584_c](./img/1584_c.png)

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:** 
```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Constraints:** 
    - `1 <= points.length <= 1000` 
    - `-10^6 <= xi, yi <= 10^6` 
    - All pairs `(xi, yi)` are distinct.
"""

from typing import List
import heapq

class Solution:
    def dist_manhattan(self, pt1: List[int], pt2: List[int]) -> int:
        return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm
        heap, visited, cost = [(0, -1, 0)], set(), 0
        while len(visited) < len(points):
            dist, i, j = heapq.heappop(heap)
            if j not in visited:
                visited.add(j)
                cost += dist
                for k in range(len(points)):
                    if k not in visited:
                        heapq.heappush(heap, (self.dist_manhattan(points[j], points[k]), j, k))
        return cost

# 20
print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))

# 18
print(Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))

# 3
print(Solution().minCostConnectPoints([[0, 0], [0, 1], [1, 0], [1, 1]]))

# 0
print(Solution().minCostConnectPoints([[0, 0]]))

