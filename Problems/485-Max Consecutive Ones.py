
"""
# Max Consecutive Ones

Given a binary array `nums`, return *the maximum number of consecutive `1`'s in the array*.

**Example 1:** 
```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

**Example 2:** 
```
Input: nums = [1,0,1,1,0,1]
Output: 2
```

**Constraints:** 
    - `1 <= nums.length <= 10^5` 
    - `nums[i]` is either `0` or `1`.

**Hint #1** 
You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # # Use a window
        # ans, i, j, n = 0, 0, 0, len(nums)
        # while i < n:
        #     if nums[i] == 1:
        #         j = i + 1
        #         while j < n and nums[j] == 1:
        #             j += 1
        #         ans = max(ans, j - i)
        #         i = j
        #     i += 1
        # return ans
        
        # Split the array by 0, and then return the length of the longest segment
        return max(map(len, "".join(map(str, nums)).split('0')))

# 3
print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))

# 2
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))

