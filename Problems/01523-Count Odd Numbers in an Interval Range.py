
"""
# Count Odd Numbers in an Interval Range

Given two non-negative integers `low` and `high`. Return the *count of odd numbers between `low` and `high` (inclusive)*.


**Example 1:** 
```
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
```

**Example 2:** 
```
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
```

**Constraints:** 
    - `0 <= low <= high <= 10^9` 
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + (low % 2)) // 2 + (high - low + (low % 2)) % 2

# 3
print(Solution().countOdds(3, 7))

# 1
print(Solution().countOdds(8, 10))

# 1
print(Solution().countOdds(0, 1))

# 1
print(Solution().countOdds(0, 2))

# 1
print(Solution().countOdds(1, 2))

# 0
print(Solution().countOdds(2, 2))

