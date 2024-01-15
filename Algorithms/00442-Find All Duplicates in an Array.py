
"""
# Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ *n* (*n* = size of array), some elements appear **twice** and others appear **once**.

Find all the elements that appear **twice** in this array.

Could you do it without extra space and in O(*n*) runtime?

**Example:** 
```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```
"""

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # # O(n) space
        # s = set(nums)
        # for x in nums:
        #     if x in s:
        #         s.remove(x)
        #     else:
        #         s.add(x)
        # return list(s)
    
        # O(1) space
        # Reference: https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/775738/Python-2-solutions-with-O(n)-timeO(1)-space-explained
        # Since all numbers are in range [1, len(nums)], therefore, 
        # if we place number i in the ith position for all numbers in 
        # the array, numbers that are in the wrong position will be 
        # the duplicated ones
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [nums[i] for i in range(len(nums)) if nums[i] - 1 != i]

print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))	# [3, 2]

