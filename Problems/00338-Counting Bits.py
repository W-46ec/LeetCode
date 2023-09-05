
"""
# Counting Bits

Given an integer `n`, return *an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the **number of** `1`'s in the binary representation of `i`.


**Example 1:** 
```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

**Example 2:** 
```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

**Constraints:** 
    - `0 <= n <= 10^5` 


**Follow up:** 
    - It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?
    - Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Consider the following binary representation: (b_k, b_k-1, ..., b_1, b_0), where b_i is either 0 or 1.

        We have the following properties:
            When decimal number i is in the range 1 <= i <= 1, b_0 is equal to 1;
            When decimal number i is in the range 2 <= i <= 3, b_1 is equal to 1;
            When decimal number i is in the range 4 <= i <= 7, b_2 is equal to 1;
            ...
            When decimal number i is in the range 2 ^ k <= i <= 2 ^ (k + 1) - 1, b_k is equal to 1;

        So, if we have the solution for numbers in range 0 <= i <= 2 ^ (k + 1) - 1 (namaly S_k), 
        we can easily obtain the solution for numbers in range 2 ^ (k + 1) <= i <= 2 ^ (k + 2) - 1
        by adding 1 to every element in S_k, because each number in range 2 ^ (k + 1) <= i <= 2 ^ (k + 2) - 1
        has exactly one extra binary '1' compared to numbers in range 0 <= i <= 2 ^ (k + 1) - 1
        (i.e., setting b_k to 1).

        For example, the base case if when i = 0, solution S_0 is [0].
        When 1 <= i <= 1, we add 1 to every element in S_0 = [0], which gives us [1] (since we are setting b_0 to 1).
        So S_1 (i.e., 0 <= i <= 1) is the concatenation of S_0 and [1], which is [0, 1].
        When 2 <= i <= 3, we add 1 to every element in S_1 = [0, 1], which gives us [1, 2] (we are setting b_1 to 1).
        So S_2 (i.e., 0 <= i <= 3) is the concatenation of S_1 and [1, 2], which is [0, 1, 1, 2].
        ...
        We may keep doing this until we cover n.
        """
        ans, exp = [0], 0
        while 2 ** exp - 1 < n:
            ans += [x + 1 for x in ans]
            exp += 1
        return ans[ : n + 1]

# [0]
print(Solution().countBits(0))

# [0, 1]
print(Solution().countBits(1))

# [0, 1, 1]
print(Solution().countBits(2))

# [0, 1, 1, 2]
print(Solution().countBits(3))

# [0, 1, 1, 2, 1]
print(Solution().countBits(4))

# [0, 1, 1, 2, 1, 2]
print(Solution().countBits(5))

# for i, n in enumerate(Solution().countBits(100)):
#     print(i, n)
