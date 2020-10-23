
"""
# Asteroid Collision

We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


**Example 1:** 
```
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
```

**Example 2:** 
```
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
```

**Example 3:** 
```
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
```

**Example 4:** 
```
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
```

**Constraints:** 
    - `1 <= asteroids <= 10^4` 
    - `-1000 <= asteroids[i] <= 1000` 
    - `asteroids[i] != 0` 

**Hint #1** 
Say a row of asteroids is stable. What happens when a new asteroid is added on the right?
"""

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            while stack and x < 0 and stack[-1] > 0:
                if stack[-1] < abs(x):
                    stack.pop()
                    continue
                elif stack[-1] == abs(x):
                    stack.pop()
                break
            else:
                stack += [x]
        return stack

# [5, 10]
print(Solution().asteroidCollision([5, 10, -5]))

# []
print(Solution().asteroidCollision([8, -8]))

# [10]
print(Solution().asteroidCollision([10, 2, -5]))

# [-2, -1, 1, 2]
print(Solution().asteroidCollision([-2, -1, 1, 2]))

# [-2, -2, -2]
print(Solution().asteroidCollision([-2, -2, 1, -2]))

