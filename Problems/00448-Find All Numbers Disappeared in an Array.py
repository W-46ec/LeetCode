
"""
# Find All Numbers Disappeared in an Array

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range `[1, n]` that do not appear in `nums`*.


**Example 1:** 
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

**Example 2:** 
```
Input: nums = [1,1]
Output: [2]
```

**Constraints:** 
    - `n == nums.length` 
    - `1 <= n <= 10^5` 
    - `1 <= nums[i] <= n` 

**Follow up**: Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.
"""

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # # O(n) space solution
        # return set(range(1, len(nums) + 1)) - set(nums)

        # O(1) space solution
        for i in range(len(nums)):
            curr_idx = abs(nums[i]) - 1
            while nums[curr_idx] > 0:
                nums[curr_idx] *= -1
                curr_idx = nums[curr_idx] * (-1) - 1
        return [(i + 1) for i in range(len(nums)) if nums[i] > 0]

# [5, 6]
print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

# [2]
print(Solution().findDisappearedNumbers([1, 1]))

