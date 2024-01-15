
"""
# Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return *the `k` most frequent elements*. You may return the answer in **any order**.


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

**Constraints:** 
    - `1 <= nums.length <= 10^5` 
    - `-10^4 <= nums[i] <= 10^4` 
    - `k` is in the range `[1, the number of unique elements in the array]`.
    - It is **guaranteed** that the answer is **unique**.

**Follow up**: Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.
"""

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Sorting -- O(nlogn)
        # counts = Counter(nums)
        # k_most_frequent = sorted([(counts[x], x) for x in counts], reverse = True)[ : k]
        # return [x for _, x in k_most_frequent]

        # Heap -- O(nlogn)
        heap = []
        counts = Counter(nums)
        for x in counts:
            heapq.heappush(heap, (-counts[x], x))
        return [heapq.heappop(heap)[1] for _ in range(k)]

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))   # [1, 2]
print(Solution().topKFrequent([1], 1))                  # [1]

