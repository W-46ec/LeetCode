
"""
# Smallest Rectangle Enclosing Black Pixels

You are given an `m x n` binary matrix `image` where `0` represents a white pixel and `1` represents a black pixel.

The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

Given two integers `x` and `y` that represents the location of one of the black pixels, return *the area of the smallest (axis-aligned) rectangle that encloses all black pixels*.

You must write an algorithm with less than `O(mn)` runtime complexity


**Example 1:** 
![302_pixel-grid](./img/302_pixel-grid.jpg)
```
Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
Output: 6
```

**Example 2:** 
```
Input: image = [["1"]], x = 0, y = 0
Output: 1
```

**Constraints:** 
    - `m == image.length` 
    - `n == image[i].length` 
    - `1 <= m, n <= 100` 
    - `image[i][j]` is either `'0'` or `'1'`.
    - `1 <= x < m` 
    - `1 <= y < n` 
    - `image[x][y] == '1'`.
    - The black pixels in the `image` only form **one component**.
"""

from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        r, u, l, d = -1, float('inf'), float('inf'), -1
        queue = [(x, y)]
        visited = [[False] * n for _ in range(m)]
        visited[x][y] = True
        while queue:
            i, j = queue.pop(0)
            r, l = max(r, j), min(l, j)
            u, d = min(u, i), max(d, i)
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                if 0 <= i + di < m and 0 <= j + dj < n \
                        and image[i + di][j + dj] == "1" \
                        and not visited[i + di][j + dj]:
                    queue += [(i + di, j + dj)]
                    visited[i + di][j + dj] = True
        return (r - l + 1) * (d - u + 1)

# 6
print(Solution().minArea([
    ["0", "0", "1", "0"], 
    ["0", "1", "1", "0"], 
    ["0", "1", "0", "0"]
], 0, 2))

# 1
print(Solution().minArea([
    ["1"]
], 0, 0))

