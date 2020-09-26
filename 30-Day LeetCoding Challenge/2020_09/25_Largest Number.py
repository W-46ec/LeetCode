
"""
# Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

**Example 1:** 
```
Input: [10,2]
Output: "210"
```

**Example 2:** 
```
Input: [3,30,34,5,9]
Output: "9534330"
```

**Note:** The result may be very large, so you need to return a string instead of an integer.
"""

from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1, s2):
            if s1 + s2 < s2 + s1:
                return 1
            elif s1 + s2 == s2 + s1:
                return 0
            return -1
        return str(int("".join(sorted(map(str, nums), key = cmp_to_key(compare)))))

# "210"
print(Solution().largestNumber([10, 2]))

# "9534330"
print(Solution().largestNumber([3, 30, 34, 5, 9]))

