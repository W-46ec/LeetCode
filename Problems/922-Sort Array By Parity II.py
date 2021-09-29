
"""
# Sort Array By Parity II

Given an array of integers `nums`, half of the integers in `nums` are **odd**, and the other half are **even**.

Sort the array so that whenever `nums[i]` is odd, `i` is **odd**, and whenever `nums[i]` is even, `i` is **even**.

Return *any answer array that satisfies this condition*.


**Example 1:** 
```
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

**Example 2:** 
```
Input: nums = [2,3]
Output: [2,3]
```

**Constraints:** 
    - `2 <= nums.length <= 2 * 10^4` 
    - `nums.length` is even.
    - Half of the integers in `nums` are even.
    - `0 <= nums[i] <= 1000`

**Follow Up**: Could you solve it in-place?
"""

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # Maintain two pointers
        # One for the odd indices/numbers
        # The other one for the even indices/numbers
        even_ptr, odd_ptr, n = 0, 1, len(nums)
        
        # Traverse through the array and modify it in-place
        while even_ptr < n and odd_ptr < n:
            # Search through the even indices, 
            # until we find an odd number at the even position
            while even_ptr < n and nums[even_ptr] % 2 == 0:
                even_ptr += 2
            
            # Similarly, search through the odd indices, 
            # until we find an even number at the odd position
            while odd_ptr < n and nums[odd_ptr] % 2 == 1:
                odd_ptr += 2

            # If both of the pointers did not go beyond the length of the array, 
            # we swap the two numbers that are in the wrong positions
            if odd_ptr < n and even_ptr < n:
                nums[odd_ptr], nums[even_ptr] = nums[even_ptr], nums[odd_ptr]

        return nums

# [4, 5, 2, 7]
print(Solution().sortArrayByParityII([4, 2, 5, 7]))

# [2, 3]
print(Solution().sortArrayByParityII([2, 3]))

