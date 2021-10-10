
"""
# Maximum Size Subarray Sum Equals k

Given an integer array `nums` and an integer `k`, return *the maximum length of a subarray that sums to `k`*. If there isn't one, return `0` instead.


**Example 1:** 
```
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
```

**Example 2:** 
```
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
```

**Constraints:** 
    - `1 <= nums.length <= 2 * 10^5` 
    - `-10^4 <= nums[i] <= 10^4` 
    - `-10^9 <= k <= 10^9` 

**Hint #1** 
Try to compute a sum of a subsequence very fast, i.e in *O(1)* … Think of prefix sum array.

**Hint #2** 
Given *S[i]* a partial sum that starts at position *0* and ends at *i*, what can *S[i - k]* tell you?

**Hint #3** 
Use HashMap + prefix sum array.
"""

from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Assume we have a prefix sum array such that 
        # prefixSum[i] is the sum of the first i elements in nums.
        # Then the problem is similar to the Two Sum problem:
        # Find indices i, j such that prefixSum[j] - prefixSum[i] is k.
        # We don't  actually have to store the whole prefixSum array.
        # We can compute the needed element while iterating through nums.
        indicesMap = {}
        i, j, prefixSum_i = 0, -1, 0
        for idx in range(len(nums)):

            # Calculate the ith value of prefixSum[]
            prefixSum_i += nums[idx]
            
            # If prefixSum[idx] is k, then nums[0 : idx + 1] is the
            # longest subarray
            if prefixSum_i == k:
                i, j = 0, idx
            
            # We want to check if we have previously seen a prefixSum[i]
            # such that prefixSum[idx] - prefixSum[i] == k
            # i.e., prefixSum[i] == prefixSum[idx] - k
            wanted = prefixSum_i - k
            if wanted in indicesMap:
                # We have seen such prefixSum[i] before
                if idx - indicesMap[wanted] + 1 > j - i + 1:
                    # Note that prefixSum[j] - prefixSum[i] 
                    # is sum(nums[i + 1], nums[i + 2], ..., nums[j])
                    i, j = indicesMap[wanted] + 1, idx
            
            # Store the current sum in the hashmap so that
            # if it is what we need in the subsequent steps,
            # we can access it in O(1) time.
            # Note that if the same value has been seen before, we
            # should keep the smaller index so that the resulting
            # subarray is the longest
            if prefixSum_i not in indicesMap:
                indicesMap[prefixSum_i] = idx

        return j - i + 1

# 4
print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))

# 2
print(Solution().maxSubArrayLen([-2, -1, 2, 1], 1))

# 0
print(Solution().maxSubArrayLen([1], 0))

# 2
print(Solution().maxSubArrayLen([1, 0, -1], -1))

