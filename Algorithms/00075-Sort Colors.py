
"""
# Sort Colors

Given an array `nums` with `n` objects colored red, white, or blue, sort them [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


**Example 1:** 
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Example 2:** 
```
Input: nums = [2,0,1]
Output: [0,1,2]
```

**Example 3:** 
```
Input: nums = [0]
Output: [0]
```

**Example 4:** 
```
Input: nums = [1]
Output: [1]
```

**Constraints:** 
    - `n == nums.length` 
    - `1 <= n <= 300` 
    - `nums[i]` is `0`, `1`, or `2`.

**Follow up**: Could you come up with a one-pass algorithm using only constant extra space?


**Hint 1** 
A rather straight forward solution is a two-pass algorithm using counting sort.

**Hint 2** 
Iterate the array counting number of 0's, 1's, and 2's.

**Hint 3** 
Overwrite array with the total number of 0's, then 1's and followed by 2's.
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # One-pass solution
        # After sorting, all red objects should be at the front.
        # All blue objects are at the back 
        # and the white ones are in the middle.
        
        # Maintain two pointers lo, hi:
        #     - lo <- the position of the last red object + 1
        #     - hi <- the position of the first blue object - 1

        # Traverse through the list. When we see a red object, place
        # it at 'lo' and move 'lo' to the right by 1. 
        # Similarly, when we see a blue object, place it at 'hi' and move
        # 'hi' to the left by 1.

        lo, hi, idx = 0, len(nums) - 1, 0
        while idx <= hi:
            if nums[idx] == 0:      # Red object
                nums[idx], nums[lo] = nums[lo], nums[idx]
                lo += 1
                idx = max(idx, lo)
            elif nums[idx] == 2:    # Blue object
                nums[idx], nums[hi] = nums[hi], nums[idx]
                hi -= 1
            else:   # White object
                idx += 1


lst = [2, 0, 2, 1, 1, 0]
print(lst, '-->', end = ' ')
Solution().sortColors(lst)
print(lst)

lst = [1, 2, 2, 2, 2, 0, 0, 0, 1, 1]
print(lst, '-->', end = ' ')
Solution().sortColors(lst)
print(lst)

