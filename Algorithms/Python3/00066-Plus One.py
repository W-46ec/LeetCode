
"""
# Plus One

Given a **non-empty** array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

**Example 1:** 
```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

**Example 2:** 
```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # # Convert to integer, add one to it, and split the digits
        # from functools import reduce
        # return [int(c) for c in list(str(reduce(lambda x, y: 10 * x + y, digits) + 1))]

        # Regular way
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
        digits = ([carry] if carry == 1 else []) + digits
        return digits

print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([9]))
