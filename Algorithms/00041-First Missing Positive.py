
"""
# First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

**Example 1:** 
```
Input: [1,2,0]
Output: 3
```

**Example 2:** 
```
Input: [3,4,-1,1]
Output: 2
```

**Example 3:** 
```
Input: [7,8,9,11,12]
Output: 1
```

**Follow up:** 
Your algorithm should run in *O(n)* time and uses constant extra space.

**Hint #1** 
Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?

**Hint #2** 
We don't care about duplicates or non-positive integers

**Hint #3** 
Remember that O(2n) = O(n)
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(nlogn)
        lst = sorted(list(set(filter(lambda x: x > 0, nums))))
        if not lst:
            return 1
        lo, hi = min(lst), max(lst)
        if lo > 1:
            return 1
        for i in range(len(lst)):
            if lst[i] != lo + i:
                return lo + i
        return hi + 1

print(Solution().firstMissingPositive([1, 2, 0]))			# 3
print(Solution().firstMissingPositive([3, 4, -1, 1]))		# 2
print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))	# 1
print(Solution().firstMissingPositive([]))					# 1

