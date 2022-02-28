

"""
# Summary Ranges

You are given a **sorted unique** integer array `nums`.

Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:
    - `"a->b"` if `a != b` 
    - `"a"` if `a == b` 

**Example 1:** 
```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

**Example 2:** 
```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

**Constraints:** 
    - `0 <= nums.length <= 20` 
    - `-2^31 <= nums[i] <= 2^31 - 1` 
    - All the values of nums are **unique**.
    - `nums` is sorted in ascending order.
"""

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 1:
            return list(map(str, nums))
        
        ans, i = [], 0
        while i < len(nums):
            lo = i
            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                i += 1
            if i != lo:
                ans += ["%d->%d" % (nums[lo], nums[i])]
            else:
                ans += [str(nums[i])]
            i += 1
        return ans

# ["0->2", "4->5", "7"]
print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))

# ["0", "2->4", "6", "8->9"]
print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))

# ["-1"]
print(Solution().summaryRanges([-1]))

# []
print(Solution().summaryRanges([]))
