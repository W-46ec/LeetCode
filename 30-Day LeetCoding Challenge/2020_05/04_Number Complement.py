
"""
# Number Complement

Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.


**Example 1:** 
```
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
```

**Example 2:** 
```
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
```

**Constraints:** 
    - The given integer `num` is guaranteed to fit within the range of a 32-bit signed integer.
    - `num >= 1` 
    - You could assume no leading zero bit in the integer’s binary representation.
    - This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        ans, bit = 0, 0
        while num:
            if num & 0x1 == 0:
                ans |= 1 << bit
            bit += 1
            num >>= 1
        return ans

testcases = [5, 1, 7, 8, 0, 2]

for x in testcases:
    print(Solution().findComplement(x))
    """
    2
    0
    0
    7
    1
    1
    """
