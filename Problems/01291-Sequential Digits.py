
"""
# Sequential Digits

An integer has *sequential digits* if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequential digits.


**Example 1:** 
```
Input: low = 100, high = 300
Output: [123,234]
```

**Example 2:** 
```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

**Constraints:** 
    - `10 <= low <= high <= 10^9` 
"""

from typing import List
from math import ceil, log10
from functools import reduce

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # The the number of digits of the lower and upper bound
        lo, hi = ceil(log10(low)), ceil(log10(high))

        # Results
        res = []
        
        # The range of possible length (digit) of the numbers in the results
        for digit_count in range(lo, hi + 1):
            # The range of the first digit
            for first_digit in range(1, 11 - digit_count):
                seq_digit = reduce(
                    lambda x, y: x * 10 + y, 
                    range(first_digit, first_digit + digit_count)
                )
                res += [seq_digit] if low <= seq_digit <= high else []

        return res

# [123, 234]
print(Solution().sequentialDigits(100, 300))

# [1234, 2345, 3456, 4567, 5678, 6789, 12345]
print(Solution().sequentialDigits(1000, 13000))

