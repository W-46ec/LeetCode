
"""
# Majority Element II

Given an integer array of size *n*, find all elements that appear more than `⌊ n/3 ⌋` times.

**Note:** The algorithm should run in linear time and in O(1) space.

**Example 1:** 
```
Input: [3,2,3]
Output: [3]
```

**Example 2:** 
```
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```

**Hint #1** 
How many majority elements could it possibly have?
Do you have a better hint? [Suggest it!](admin@leetcode.com) 
"""

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # # O(n) time & O(n) space
        # counter = Counter(nums)
        # return list(filter(lambda x: counter[x] > len(nums) // 3, counter.keys()))

        # O(n) time & O(1) space
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for x in nums:
            if x == candidate1:
                count1 += 1
            elif x == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = x, 1
            elif count2 == 0:
                candidate2, count2 = x, 1
            else:
                count1 -= 1
                count2 -= 1
        return [x for x in [candidate1, candidate2] if nums.count(x) > len(nums) // 3]

# [3]
print(Solution().majorityElement([3, 2, 3]))

# [1, 2]
print(Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))

# []
print(Solution().majorityElement([1, 2, 3]))

# [3]
print(Solution().majorityElement([1, 2, 2, 3, 3, 3]))

