
"""
# Sort Array By Parity

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return ***any array** that satisfies this condition*.


**Example 1:** 
```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

**Example 2:** 
```
Input: nums = [0]
Output: [0]
```

**Constraints:** 
    - `1 <= nums.length <= 5000` 
    - `0 <= nums[i] <= 5000` 
"""

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # # Built-in function
        # return sorted(nums, key = lambda x: x % 2)

        # Swapping
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            while lo < hi and nums[lo] % 2 == 0:
                lo += 1
            while lo < hi and nums[hi] % 2 == 1:
                hi -= 1
            nums[lo], nums[hi] = nums[hi], nums[lo]
        return nums

# [4, 2, 1, 3]
print(Solution().sortArrayByParity([3, 1, 2, 4]))

# [0]
print(Solution().sortArrayByParity([0]))

