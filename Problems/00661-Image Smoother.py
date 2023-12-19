
"""
# Image Smoother

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
![661_smoother-grid](./img/661_smoother-grid.jpg)

Given an `m x n` integer matrix `img` representing the grayscale of an image, return *the image after applying the smoother on each cell of it*.


**Example 1:** 
![661_smooth-grid](./img/661_smooth-grid.jpg)
```
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```

**Example 2:** 
![661_smooth2-grid](./img/661_smooth2-grid.jpg)
```
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
```

**Constraints:** 
    - `m == img.length` 
    - `n == img[i].length` 
    - `1 <= m, n <= 200` 
    - `0 <= img[i][j] <= 255` 
"""

import unittest
from typing import List
from itertools import product

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        img_smooth = [[0] * n for _ in range(m)]
        for x, y in product(range(m), range(n)):
            val, count = 0, 0
            for dx, dy in product(range(-1, 2), range(-1, 2)):
                val += img[x + dx][y + dy] if 0 <= x + dx < m and 0 <= y + dy < n else 0
                count += 1 if 0 <= x + dx < m and 0 <= y + dy < n else 0
            img_smooth[x][y] = val // count
        return img_smooth


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def testcase2(self):
        self.assertEqual(self.soln_obj.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]), [[137, 141, 137], [141, 138, 141], [137, 141, 137]])


if __name__ == '__main__':
    unittest.main()
