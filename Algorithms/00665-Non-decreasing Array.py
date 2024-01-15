
"""
# Non-decreasing Array

Given an array `nums` with `n` integers, your task is to check if it could become non-decreasing by modifying **at most one element**.

We define an array is non-decreasing if `nums[i] <= nums[i + 1]` holds for every `i` (**0-based**) such that (`0 <= i <= n - 2`).


**Example 1:** 
```
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
```

**Example 2:** 
```
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
```

**Constraints:** 
    - `n == nums.length` 
    - `1 <= n <= 10^4` 
    - `-10^5 <= nums[i] <= 10^5` 
"""

# https://leetcode.com/problems/non-decreasing-array/discuss/106816/Python-Extremely-Easy-to-Understand

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        arr1, arr2 = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # In array 1, we modify the first element by making
                # the first element equal to the second element.
                # In array 2, we do the contrary (i.e., make the 
                # second element equal to the first one).
                arr1[i] = nums[i + 1]
                arr2[i + 1] = nums[i]
                break
        return arr1 == sorted(arr1) or arr2 == sorted(arr2)

# True
print(Solution().checkPossibility([4, 2, 3]))

# False
print(Solution().checkPossibility([4, 2, 1]))

# False
print(Solution().checkPossibility([3, 4, 2, 3]))
