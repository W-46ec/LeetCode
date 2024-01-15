
"""
# Contiguous Array

Given a binary array `nums`, return *the maximum length of a contiguous subarray with an equal number of `0` and `1`*.


**Example 1:** 
```
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
```

**Example 2:** 
```
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
```

**Constraints:** 
    - `1 <= nums.length <= 10^5` 
    - `nums[i]` is either `0` or `1`.
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Hashmap - O(n) time & O(n) space
        ans, m = 0, {}
        # Define a variable to keep track of the number of 1's we need
        # in each iteration
        num_one_needed = 0
        for i, val in enumerate(nums):
            # If we see a 1, we subtract 1 from num_one_needed, 
            # otherwise, we add 1 to it.
            # The value represents how many 1's we need to form an array
            # with equal number of 0 and 1 in the current iteration.
            num_one_needed -= 1 if val else -1
            
            # If the value of num_one_needed is 0, then everything
            # before the current iteration forms an array with equal 
            # num of 0 and 1.
            if num_one_needed == 0:
                ans = max(ans, i + 1)
            
            # If we have seen the same num_one_needed value in one of the
            # previous iterations, it means that the digits between these
            # two iterations form an array that satisfy the condition.
            if num_one_needed in m:
                # Take the maximum
                ans = max(ans, i - m[num_one_needed])
            else:
                # Store the unseen values in the hashmap
                m[num_one_needed] = i
        
        return ans

print(Solution().findMaxLength([0, 1]))     # 2
print(Solution().findMaxLength([0, 1, 0]))  # 2
print(Solution().findMaxLength([0, 1, 1]))  # 2

