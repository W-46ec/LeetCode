
"""
# Maximum XOR of Two Numbers in an Array

Given an integer array `nums`, return the maximum result of `nums[i] XOR nums[j]`, where `0 ≤ i ≤ j < n`.

**Follow up:** Could you do this in `O(n)` runtime?


**Example 1:** 
```
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
```

**Example 2:** 
```
Input: nums = [0]
Output: 0
```

**Example 3:** 
```
Input: nums = [2,4]
Output: 6
```

**Example 4:** 
```
Input: nums = [8,10,2]
Output: 10
```

**Example 5:** 
```
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
```

**Constraints:** 
    - `1 <= nums.length <= 2 * 104` 
    - `0 <= nums[i] <= 231 - 1` 
"""

# Reference: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/849818/Python-Two-solutions-O(N)-time-each

from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31, -1, -1):
            prefix = ans | (1 << i)
            prefixes = { prefix & x for x in nums }

            # We are looking for:
            #    (x XOR y) & prefix == prefix
            # => (x & prefix) XOR (y & prefix) == prefix
            # => y & prefix == prefix XOR (x & prefix)

            if any((prefix ^ x_pref) in prefixes for x_pref in prefixes):
                ans = prefix
        return ans

# 28
print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))

# 0
print(Solution().findMaximumXOR([0]))

# 6
print(Solution().findMaximumXOR([2, 4]))

# 10
print(Solution().findMaximumXOR([8, 10, 2]))

# 127
print(Solution().findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))

# 0
print(Solution().findMaximumXOR([2]))

# 15
print(Solution().findMaximumXOR([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

