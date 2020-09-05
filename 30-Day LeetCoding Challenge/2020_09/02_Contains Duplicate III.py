
"""
# Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices *i* and *j* in the array such that the **absolute** difference between **nums[i]** and **nums[j]** is at most *t* and the **absolute** difference between *i* and *j* is at most *k*.

**Example 1:** 
```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

**Example 2:** 
```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

**Example 3:** 
```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

**Hint #1** 
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.

**Hint #2** 
Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked. When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.
"""

from typing import List
from bisect import bisect_left

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:        
        # O(n logk) time
        window, lo, hi = [], 0, 0
        while hi < len(nums):
            if len(window) == k + 1:
                window.pop(bisect_left(window, nums[lo]))
                lo += 1
            pos = bisect_left(window, nums[hi])
            window.insert(pos, nums[hi])
            if len(window) > 1 and pos == 0 and window[1] - window[0] <= t:
                return True
            if len(window) > 1 and pos == len(window) - 1 and window[-1] - window[-2] <= t:
                return True
            if len(window) > 1 and \
                pos > 0 and pos < len(window) - 1 and \
                (window[pos] - window[pos - 1] <= t or window[pos + 1] - window[pos] <= t):
                return True
            hi += 1
        return False

print(Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))         # True
print(Solution().containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))         # True
print(Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))   # False
print(Solution().containsNearbyAlmostDuplicate([2, 0, -2, 2], 2, 1))        # False

