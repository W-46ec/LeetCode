
"""
# Build an Array With Stack Operations

Given an `array` target and an integer `n`. In each iteration, you will read a number from `list = {1,2,3..., n}`.

Build the `target` array using the following operations:
    - **Push**: Read a new element from the beginning `list`, and push it in the array.
    - **Pop**: delete the last element of the array.
    - If the target array is already built, stop reading more elements.

You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.


**Example 1:** 
```
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
```

**Example 2:** 
```
Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
```

**Example 3:** 
```
Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.
```

**Example 4:** 
```
Input: target = [2,3,4], n = 4
Output: ["Push","Pop","Push","Push","Push"]
```

**Constraints:** 
    - `1 <= target.length <= 100` 
    - `1 <= target[i] <= 100` 
    - `1 <= n <= 100` 
    - `target` is strictly increasing.
"""

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        lst = [i for i in range(1, n + 1)]
        i, j = 0, 0
        while i < len(lst) and j < len(target):
            if lst[i] < target[j]:
                ans.append("Push")
                ans.append("Pop")
            else:
                ans.append("Push")
                j += 1
            i += 1
        return ans

print(Solution().buildArray([1, 3], 3))
print(Solution().buildArray([1, 2, 3], 3))
print(Solution().buildArray([1, 2], 4))
print(Solution().buildArray([2, 3, 4], 4))

