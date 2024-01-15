
"""
# Detonate the Maximum Bombs

You are given a list of bombs. The **range** of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a **0-indexed** 2D integer array `bombs` where `bombs[i] = [xi, yi, ri]`. `xi` and `yi` denote the X-coordinate and Y-coordinate of the location of the `ith` bomb, whereas `ri` denotes the **radius** of its range.

You may choose to detonate a **single** bomb. When a bomb is detonated, it will detonate **all bombs** that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of `bombs`, return *the **maximum** number of bombs that can be detonated if you are allowed to detonate **only one** bomb*.


**Example 1:** 
![2101_desmos-eg-3](./img/2101_desmos-eg-3.png)
```
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
```

**Example 2:** 
![2101_desmos-eg-2](./img/2101_desmos-eg-2.png)
```
Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
```

**Example 3:** 
![2101_desmos-eg-1](./img/2101_desmos-eg-1.png)
```
Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.
```

**Constraints:** 
    - `1 <= bombs.length <= 100` 
    - `bombs[i].length == 3` 
    - `1 <= xi, yi, ri <= 10^5` 
"""

from typing import List
from collections import defaultdict
from math import sqrt

class Solution:
    def dist(self, x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Create a directed graph in the following way:
        # Add an edge from node i to node j iff bomb i 
        # can detonate bomb j, for any pair of bombs i, j.
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                distance = self.dist(x1, y1, x2, y2)
                graph[i] += [j] if distance <= r1 else []
                graph[j] += [i] if distance <= r2 else []

        # Run BFS from each node v to determine the number of
        # nodes can be reachable from v.
        # The number of nodes that are reachable from v is equivalent
        # to the number of bombs that can be detonated by v.
        max_bombs = -1
        for v in range(len(bombs)):
            queue, visited = [v], [False] * len(bombs)
            visited[v] = True
            for src in queue:
                for dst in graph[src]:
                    if not visited[dst]:
                        queue += [dst]
                        visited[dst] = True
            max_bombs = max(max_bombs, len(queue))
        return max_bombs

# 2
print(Solution().maximumDetonation([[2, 1, 3], [6, 1, 4]]))

# 1
print(Solution().maximumDetonation([[1, 1, 5], [10, 10, 5]]))

# 5
print(Solution().maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
