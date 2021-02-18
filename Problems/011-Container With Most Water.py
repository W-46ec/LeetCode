
"""
# Container With Most Water

Given `n` non-negative integers `a1, a2, ..., an`, where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Notice** that you may not slant the container.


**Example 1:** 
![011_question_11](./img/011_question_11.jpg)
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:** 
```
Input: height = [1,1]
Output: 1
```

**Example 3:** 
```
Input: height = [4,3,2,1,4]
Output: 16
```

**Example 4:** 
```
Input: height = [1,2,1]
Output: 2
```

**Constraints:** 
    - `n == height.length` 
    - `2 <= n <= 3 * 10^4` 
    - `0 <= height[i] <= 3 * 10^4` 

**Hint #1** 
The aim is to maximize the area formed between the vertical lines. The area of any container is calculated using the shorter line as length and the distance between the lines as the width of the rectangle.
```
Area = length of shorter vertical line * distance between lines
```
We can definitely get the maximum width container as the outermost lines have the maximum distance between them. However, this container **might not be the maximum in size** as one of the vertical lines of this container could be really short.

![011_hint_water_trap_1](./img/011_hint_water_trap_1.png)

![011_hint_water_trap_2](./img/011_hint_water_trap_2.png)

**Hint #2** 
Start with the maximum width container and go to a shorter width container if there is a vertical line longer than the current containers shorter line. This way we are compromising on the width but we are looking forward to a longer length container.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, lo, hi = 0, 0, len(height) - 1
        while lo < hi:
            ans = max((hi - lo) * min(height[lo], height[hi]), ans)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return ans


# 49
print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# 1
print(Solution().maxArea([1, 1]))

# 16
print(Solution().maxArea([4, 3, 2, 1, 4]))

# 2
print(Solution().maxArea([1, 2, 1]))

