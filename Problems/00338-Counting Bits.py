
"""
# Counting Bits

Given a non negative integer number **num**. For every numbers **i** in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.

**Example 1:** 
```
Input: 2
Output: [0,1,1]
```

**Example 2:** 
```
Input: 5
Output: [0,1,1,2,1,2]
```

**Follow up:** 
    - It is very easy to come up with a solution with run time **O(n*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass?
    - Space complexity should be **O(n)**.
    - Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.
"""

from typing import List
import numpy as np

class Solution:
    def countBits(self, num: int) -> List[int]:
        # # O(n * sizeof(integer))
        # ans = []
        # for i in range(num + 1):
        #     curr = 0
        #     while i > 0:
        #         curr += 0x1 & i
        #         i >>= 1
        #     ans.append(curr)
        # return ans

        # O(n)
        # ans, exp = [0, 1], 1
        # while 2 ** exp - 1 < num:
        #     arr = ans[2 ** (exp - 1) : 2 ** exp]
        #     ans += arr + [x + 1 for x in arr]
        #     exp += 1
        # return ans[ : num + 1]

        # O(n) - Using numpy
        ans, exp = np.arange(2, dtype = 'int'), 1
        while 2 ** exp - 1 < num:
            ans = np.concatenate((ans, ans + 1))
            exp += 1
        return ans[ : num + 1]

print(Solution().countBits(0))
print(Solution().countBits(1))
print(Solution().countBits(2))
print(Solution().countBits(3))
print(Solution().countBits(4))
print(Solution().countBits(5))

# for i, n in enumerate(Solution().countBits(100)):
#     print(i, n)
