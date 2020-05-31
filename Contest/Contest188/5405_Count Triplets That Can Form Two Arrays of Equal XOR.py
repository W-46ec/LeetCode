
"""
# Count Triplets That Can Form Two Arrays of Equal XOR

Given an array of integers `arr`.

We want to select three indices `i`, `j` and `k` where `(0 <= i < j <= k < arr.length)`.

Let's define `a` and `b` as follows:
    - `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]` 
    - `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]` 

Note that **^** denotes the **bitwise-xor** operation.

Return the number of triplets (`i`, `j` and `k`) Where `a == b`.


**Example 1:** 
```
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
```

**Example 2:** 
```
Input: arr = [1,1,1,1,1]
Output: 10
```

**Example 3:** 
```
Input: arr = [2,3]
Output: 0
```

**Example 4:** 
```
Input: arr = [1,3,5,7,9]
Output: 3
```

**Example 5:** 
```
Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8
```

**Constraints:** 
    - `1 <= arr.length <= 300` 
    - `1 <= arr[i] <= 10^8` 
"""

from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans, a, b = 0, 0, 0
        for i in range(len(arr)):
            a = arr[i]
            for j in range(i + 1, len(arr)):
                b = arr[j]
                for k in range(j, len(arr)):
                    if k > j:
                        b ^= arr[k]
                    if a == b:
                        ans += 1
                a ^= arr[j]
        return ans
        
        # # Time Limit Exceeded
        # from functools import reduce
        # ans = 0
        # for i in range(len(arr)):
        #     for j in range(i + 1, len(arr)):
        #         for k in range(j, len(arr)):
        #             a = reduce(lambda x, y: x ^ y, arr[i : j])
        #             b = reduce(lambda x, y: x ^ y, arr[j : k + 1])
        #             if a == b:
        #                 ans += 1
        # return ans

print(Solution().countTriplets([2, 3, 1, 6, 7]))    # 4
print(Solution().countTriplets([1, 1, 1, 1, 1]))    # 10
print(Solution().countTriplets([2, 3]))             # 0
print(Solution().countTriplets([1, 3, 5, 7, 9]))    # 3
print(Solution().countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]))    # 8

# 762
print(Solution().countTriplets([808, 874, 66, 212, 150, 827, 941, 951, 26, 906, 912, 332, 732, 319, 995, 119, 916, 890, 238, 385, 367, 806, 585, 451, 906, 699, 305, 476, 237, 823, 986, 794, 192, 237, 45, 671, 690, 100, 726, 936, 382, 610, 796, 674, 446, 486, 88, 433, 489, 319, 214, 117, 163, 148, 55, 735, 744, 92, 692, 611, 215, 519, 720, 620, 188, 477, 353, 6, 359, 896, 743, 490, 781, 743, 490, 9, 483, 815, 716, 71, 651, 65, 714, 207, 517, 124, 633, 623, 22, 768, 790, 296, 574, 289, 799, 186, 933, 514, 423, 301, 138, 99, 233, 910, 871, 48, 855, 532, 323, 168, 491, 914, 633, 124, 517, 258, 775, 326, 577, 127, 574, 770, 316, 835, 639, 828, 323, 177, 498, 366, 156, 644, 536, 920, 384, 133, 261, 181, 432, 951, 519, 903, 384, 93, 477, 400, 77, 647, 714, 645, 79, 451, 396, 959, 563, 332, 895, 81, 814, 31, 817, 702, 399]))
