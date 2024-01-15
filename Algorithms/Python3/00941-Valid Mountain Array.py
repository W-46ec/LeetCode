
"""
# Valid Mountain Array

Given an array of integers `arr`, return *`true` if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:
    - `arr.length >= 3` 
    - There exists some `i` with `0 < i < arr.length - 1` such that:
        - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]` 
        - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]` 

![941_hint_valid_mountain_array](./img/941_hint_valid_mountain_array.png)

**Example 1:** 
```
Input: arr = [2,1]
Output: false
```

**Example 2:** 
```
Input: arr = [3,5,5]
Output: false
```

**Example 3:** 
```
Input: arr = [0,3,2,1]
Output: true
```

**Constraints:**
    - `1 <= arr.length <= 10^4` 
    - `0 <= arr[i] <= 10^4` 

**Hint 1** 
It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just need to be able to determine the start of the valley in the mountain and from that point onwards, it should be a valley i.e. no mini-hills after that. Use this information in regards to the values in the array and you will be able to come up with a straightforward solution.
"""

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        
        # Increasing phase
        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            i += 1
        
        # There are two possible cases where we can stop early:
        #     1. i == 0 -- There was no strictly increasing part
        #     2. i == len(arr) - 1 -- There will be no decreasing part
        if i == 0 or i == len(arr) - 1:
            return False
        
        # Decreasing phase
        while i < len(arr) - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        # If 'i' did not reach the end of the array, it means
        # some constraints were violated in the decreasing phase.
        return i == len(arr) - 1

# False
print(Solution().validMountainArray([2, 1]))

# False
print(Solution().validMountainArray([1]))

