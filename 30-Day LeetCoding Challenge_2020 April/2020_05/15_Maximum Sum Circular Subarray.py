
"""
# Maximum Sum Circular Subarray

Given a **circular array C** of integers represented by `A`, find the maximum possible sum of a non-empty subarray of **C**.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, `C[i] = A[i]` when `0 <= i < A.length`, and `C[i+A.length] = C[i]` when `i >= 0`.)

Also, a subarray may only include each element of the fixed buffer `A` at most once.  (Formally, for a subarray `C[i], C[i+1], ..., C[j]`, there does not exist `i <= k1, k2 <= j` with `k1 % A.length = k2 % A.length`.)


**Example 1:** 
```
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
```

**Example 2:** 
```
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
```

**Example 3:** 
```
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
```

**Example 4:** 
```
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
```

**Example 5:** 
```
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
```

Note:
    1. -30000 <= A[i] <= 30000
    2. 1 <= A.length <= 30000
"""


# Reference: https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/

from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(arr):
            if len(arr) <= 0:
                return None
            currentMax = arr[0]
            currentSum = arr[0]
            for i in range(1, len(arr)):
                if currentSum < 0:
                    currentSum = arr[i]
                else:
                    currentSum += arr[i]
                currentMax = max(currentMax, currentSum)
            return currentMax
        
        # case 1
        sum1 = kadane(A)
        
        # case 2
        sum2 = sum(A) + kadane([-x for x in A])
        
        allNegative = True
        for x in A:
            if x > 0:
                allNegative = False

        return max(sum1, sum2) if not allNegative else sum1

print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))
print(Solution().maxSubarraySumCircular([5, -3, 5]))
print(Solution().maxSubarraySumCircular([3, -1, 2, -1]))
print(Solution().maxSubarraySumCircular([3, -2, 2, -3]))
print(Solution().maxSubarraySumCircular([-2, -3, -1]))

