
"""
# Angle Between Hands of a Clock

Given two numbers, `hour` and `minutes`. Return the smaller angle (in degrees) formed between the `hour` and the `minute` hand.


**Example 1:** 
![14_sample_1_1673](./img/14_sample_1_1673.png)
```
Input: hour = 12, minutes = 30
Output: 165
```

**Example 2:** 
![14_sample_2_1673](./img/14_sample_2_1673.png)
```
Input: hour = 3, minutes = 30
Output: 75
```

**Example 3:** 
![14_sample_3_1673](./img/14_sample_3_1673.png)
```
Input: hour = 3, minutes = 15
Output: 7.5
```

**Example 4:** 
```
Input: hour = 4, minutes = 50
Output: 155
```

**Example 5:** 
```
Input: hour = 12, minutes = 0
Output: 0
```

**Constraints:** 
    - `1 <= hour <= 12` 
    - `0 <= minutes <= 59` 
    - Answers within `10^-5` of the actual value will be accepted as correct.
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degreeH, degreeM = hour * 30 + minutes / 2, minutes * 6
        diff = abs(degreeH - degreeM)
        return min(diff, 360 - diff)

print(Solution().angleClock(12, 30))    # 165.0
print(Solution().angleClock(3, 30))     # 75.0
print(Solution().angleClock(3, 15))     # 7.5
print(Solution().angleClock(4, 50))     # 155.0
print(Solution().angleClock(12, 0))     # 0.0

