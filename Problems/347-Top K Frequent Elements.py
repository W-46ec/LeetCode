
"""
# Top K Frequent Elements

Given a non-empty array of integers, return the **k** most frequent elements.

**Example 1:** 
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:** 
```
Input: nums = [1], k = 1
Output: [1]
```

**Note:** 
    - You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
    - Your algorithm's time complexity **must be** better than O(*n* log *n*), where *n* is the array's size.
    - It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    - You can return the answer in any order.
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for x in nums:
            if x in h:
                h[x] += 1
            else:
                h[x] = 1
        return [x[0] for x in sorted([(k, h[k]) for k in h], key = lambda x: x[1], reverse = True)][ : k]

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))   # [1, 2]
print(Solution().topKFrequent([1], 1))                  # [1]

