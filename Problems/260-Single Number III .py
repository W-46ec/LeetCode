
"""
# Single Number III

Given an array of numbers `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

**Example:** 
```
Input:  [1,2,1,3,2,5]
Output: [3,5]
```

**Note:** 
    1. The order of the result is not important. So in the above example, `[5, 3]` is also correct.
    2. Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for x in nums:
            if x in s:
                s.remove(x)
            else:
                s.add(x)
        return list(s)

print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))

