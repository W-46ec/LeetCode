
"""
# Find the Smallest Divisor Given a Threshold

Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the **smallest** divisor such that the result mentioned above is less than or equal to `threshold`.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.


**Example 1:** 
```
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
```

**Example 2:** 
```
Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
```

**Example 3:** 
```
Input: nums = [19], threshold = 5
Output: 4
```

**Constraints:** 
    - `1 <= nums.length <= 5 * 10^4` 
    - `1 <= nums[i] <= 10^6` 
    - `nums.length <= threshold <= 10^6` 

**Hint #1** 
Examine every possible number for solution. Choose the largest of them.

**Hint #2** 
Use binary search to reduce the time complexity.
"""

from typing import List
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(map(lambda x: ceil(x / mid), nums)) <= threshold:
                hi = mid
            else:
                lo = mid + 1
        return hi

# 5
print(Solution().smallestDivisor([1, 2, 5, 9], 6))

# 3
print(Solution().smallestDivisor([2, 3, 5, 7, 11], 11))

# 4
print(Solution().smallestDivisor([19], 5))

# 1
print(Solution().smallestDivisor([1, 2, 3], 1000000))

# 495280
print(Solution().smallestDivisor([962551, 933661, 905225, 923035, 990560], 10))

# 10134
print(Solution().smallestDivisor([46480, 71852, 4544, 23598, 962, 66567, 66601, 90661, 30701, 30463, 76184, 35590, 50634, 82516, 3847, 83498, 40938, 82092, 17753, 21195, 3748, 94798, 77080, 49254, 24184, 81610, 80045, 69248, 10776, 45690, 59496, 15406, 38198, 47381, 13353, 93106, 71420, 14775, 99118, 6866, 62300, 57444, 3966, 91603, 56289, 26752, 16439, 96836, 80050, 14948, 14487, 3034, 79113, 23445, 78123, 91204, 77022, 36837, 38978, 94389, 77331, 523, 42947, 25830, 55630, 45936, 76823, 32614, 49959, 5111, 74080, 59558, 79203, 93414, 11356, 87885, 50858, 4490, 11503, 35141, 4446, 52051, 75511, 41767, 64622, 61572, 28298, 21584, 77878, 99083, 47585, 75926, 84968, 12477, 86333, 55299, 99291, 47402, 82539, 19070], 549))

# 1
print(Solution().smallestDivisor([1, 2, 3], 6))

