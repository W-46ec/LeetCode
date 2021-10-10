
"""
# 3Sum

Given an array `nums` of n integers, are there elements a, b, c in `nums` such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:** 
The solution set must not contain duplicate triplets.

**Example:** 
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```


**Hint #1** 
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!

**Hint #2** 
For the two-sum problem, if we fix one of the numbers, say
```
x
```

, we have to scan the entire array to find the next number
```
y
```

which is
```
value - x
```

where value is the input parameter. Can we change our array somehow so that this search becomes faster?

**Hint #3** 
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans, i = [], 0
        while i < len(nums) - 2:
            # Skip the repeated numbers
            while i > 0 and i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            lo, hi = i + 1, len(nums) - 1  # Define two pointers
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == 0:  # Found a solution
                    ans.append([nums[i], nums[lo], nums[hi]])

                    # Again, skip the repeated numbers
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1

                elif s < 0: # "Too negative", maybe we should move lo to the right a bit to make it more positive
                    lo += 1
                else:       # s > 0 -- "Too positive", so maybe we should adjust hi to get a smaller number
                    hi -= 1
            i += 1
        return ans

# ANS: [[-1, -1, 2], [-1, 0, 1]]
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

# ANS: [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
print(Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))

