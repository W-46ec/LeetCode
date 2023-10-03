
"""
# Number of Good Pairs

Given an array of integers `nums`, return *the number of **good pairs***.

A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i` < `j`.


**Example 1:** 
```
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
```

**Example 2:** 
```
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
```

**Example 3:** 
```
Input: nums = [1,2,3]
Output: 0
```

**Constraints:** 
    - `1 <= nums.length <= 100` 
    - `1 <= nums[i] <= 100` 
"""

from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Count the occurrences of each integer in nums.

        For any integer k, if it appears in nums x times, it will be able to 
        form (1 + 2 + ... + (x - 2) + (x - 1)) which is [x * (x - 1)] / 2 good pairs.
        Note that if x is 1 (i.e., integer k only appears once in nums), 0 good pairs
        can be formed.

        Sum up the number of good pairs for each distinct integer in nums.
        """
        return sum(map(lambda x: x * (x - 1) // 2, Counter(nums).values()))


# 4
print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))

# 6
print(Solution().numIdenticalPairs([1, 1, 1, 1]))

# 0
print(Solution().numIdenticalPairs([1, 2, 3]))
