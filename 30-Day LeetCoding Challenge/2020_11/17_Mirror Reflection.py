
"""
# Mirror Reflection

There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered `0`, `1`, and `2`.

The square room has walls of length `p`, and a laser ray from the southwest corner first meets the east wall at a distance `q` from the `0`th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)


**Example 1:** 
```
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
![17_reflection](./img/17_reflection.png)
```

**Note:** 
    1. `1 <= p <= 1000` 
    2. `0 <= q <= p` 
"""

# Reference: https://leetcode.com/problems/mirror-reflection/solution/

from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p = (p // g) % 2
        q = (q // g) % 2
        return 1 if p and q else 0 if p else 2

print(Solution().mirrorReflection(2, 1))    # 2
print(Solution().mirrorReflection(3, 2))    # 0
print(Solution().mirrorReflection(4, 4))    # 1


