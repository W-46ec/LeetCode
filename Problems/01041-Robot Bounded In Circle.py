
"""
# Robot Bounded In Circle

On an infinite plane, a robot initially stands at `(0, 0)` and faces north.  The robot can receive one of three instructions:
    - `"G"`: go straight 1 unit;
    - `"L"`: turn 90 degrees to the left;
    - `"R"`: turn 90 degress to the right.

The robot performs the `instructions` given in order, and repeats them forever.

Return `true` if and only if there exists a circle in the plane such that the robot never leaves the circle.


**Example 1:** 
```
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
```

**Example 2:** 
```
Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
```

**Example 3:** 
```
Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
```

**Note:** 
    1. `1 <= instructions.length <= 100` 
    2. `instructions[i]` is in `{'G', 'L', 'R'}` 


**Hint #1** 
Calculate the final vector of how the robot travels after executing all instructions once - it consists of a change in position plus a change in direction.

**Hint #2** 
The robot stays in the circle iff (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        rotation = { 'L': -1, 'R': 1 }
        direction, pos = 0, [0, 0]
        for ins in instructions:
            if ins == 'G':
                pos = list(map(lambda x, y: x + y, pos, moves[direction]))
            else:
                direction = (direction + rotation[ins]) % len(moves)
        return pos == [0, 0] or direction != 0

print(Solution().isRobotBounded("GGLLGG"))      # True
print(Solution().isRobotBounded("GG"))          # False
print(Solution().isRobotBounded("GL"))          # True
print(Solution().isRobotBounded("GLRLLGLL"))    # True

