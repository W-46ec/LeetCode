
"""
# Check If All 1's Are at Least Length K Places Away

Given an array `nums` of 0s and 1s and an integer `k`, return `True` if all 1's are at least `k` places away from each other, otherwise return `False`.


**Example 1:** 
![1437_sample_1_1791](./img/1437_sample_1_1791.png)
```
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
```

**Example 2:** 
![1437_sample_2_1791](./img/1437_sample_2_1791.png)
```
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
```

**Example 3:** 
```
Input: nums = [1,1,1,1,1], k = 0
Output: true
```

**Example 4:** 
```
Input: nums = [0,1,0,1], k = 1
Output: true
```

**Constraints:** 
    - `1 <= nums.length <= 10^5` 
    - `0 <= k <= nums.length` 
    - `nums[i]` is `0` or `1` 

**Hint #1** 
Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.
"""

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = float('-inf')
        for idx, x in enumerate(nums):
            if x == 1:
                if idx - prev <= k:
                    return False
                prev = idx
        return True

# True
print(Solution().kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))

# False
print(Solution().kLengthApart([1, 0, 0, 0, 1, 0, 1], 2))

# True
print(Solution().kLengthApart([1, 1, 1, 1, 1], 0))

# True
print(Solution().kLengthApart([0, 1, 0, 1], 1))
