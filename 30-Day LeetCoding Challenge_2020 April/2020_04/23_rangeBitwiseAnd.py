
"""
# Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n &= n - 1
        return m & n

        # # Wrong
        # ans, length = 0x0, len(bin(n)) - 2
        # lo, hi = 2 ** (length - 1), 2 ** length - 1
        # for i in range(length - 1, -1, -1):
        #     if lo <= m and n <= hi:
        #         ans |= 0x1 << i
        #     lo, hi = lo + 2 ** (i - 1), hi + 2 ** i - 1
        # return ans

        # # Time Limit Exceeded
        # return reduce(lambda x, y: x & y, range(m, n + 1))

print(Solution().rangeBitwiseAnd(3, 3))
print(Solution().rangeBitwiseAnd(5, 5))
print(Solution().rangeBitwiseAnd(4, 7))
print(Solution().rangeBitwiseAnd(5, 7))
print(Solution().rangeBitwiseAnd(6, 7))
print(Solution().rangeBitwiseAnd(0, 1))
print(Solution().rangeBitwiseAnd(0, 2147483645))
print(Solution().rangeBitwiseAnd(600000000, 2147483645))
