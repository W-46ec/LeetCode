
"""
# Move Zeroes

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.


**Example 1:** 
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Example 2:** 
```
Input: nums = [0]
Output: [0]
```

**Constraints:** 
    - `1 <= nums.length <= 10^4` 
    - `-2^31 <= nums[i] <= 2^31 - 1` 

**Follow up**: Could you minimize the total number of operations done?
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Method 1
        # i, j = 0, 0
        # while j < len(nums):
        #     if nums[j] != 0:
        #         nums[i] = nums[j]
        #         i += 1
        #     j += 1
        # while i < len(nums):
        #     nums[i] = 0
        #     i += 1

        # # Method 2
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        
        # Method 3
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1

# [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
lst = [0, 1, 0, 3, 12]
print(lst, end = ' -> ')
Solution().moveZeroes(lst)
print(lst)

# [0] -> [0]
lst = [0]
print(lst, end = ' -> ')
Solution().moveZeroes(lst)
print(lst)

# [2, 1] -> [2, 1]
lst = [2, 1]
print(lst, end = ' -> ')
Solution().moveZeroes(lst)
print(lst)

