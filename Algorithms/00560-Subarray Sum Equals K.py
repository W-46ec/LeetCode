
"""
# Subarray Sum Equals K

Given an array of integers `nums` and an integer `k`, return *the total number of continuous subarrays whose sum equals to `k`*.


**Example 1:** 
```
Input: nums = [1,1,1], k = 2
Output: 2
```

**Example 2:** 
```
Input: nums = [1,2,3], k = 3
Output: 2
```

**Constraints:** 
    - `1 <= nums.length <= 2 * 10^4` 
    - `-1000 <= nums[i] <= 1000` 
    - `-10^7 <= k <= 10^7` 

**Hint 1** 
Will Brute force work here? Try to optimize it.

**Hint 2** 
Can we optimize it by using some extra space?

**Hint 3** 
What about storing sum frequencies in a hash table? Will it be useful?

**Hint 4** 
sum(i, j) = sum(0, j) - sum(0, i), where sum(i, j) represents the sum of all the elements from index i to j - 1. Can we use this property to optimize it.
"""

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        
        seen, cumm_sum, ans = defaultdict(int), 0, 0
        for val in nums:
            cumm_sum += val
            ans += 1 if cumm_sum == k else 0
            ans += seen[cumm_sum - k]
            seen[cumm_sum] += 1
        return ans

# 2
print(Solution().subarraySum([1, 1, 1], 2))

# 2
print(Solution().subarraySum([1, 2, 3], 3))
