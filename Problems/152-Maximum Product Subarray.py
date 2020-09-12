
"""
# Maximum Product Subarray

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Example 1:** 
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:** 
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
"""

# Reference: https://leetcode.com/problems/maximum-product-subarray/discuss/841176/Python-dp-solution-explained

class Solution:
    def maxProduct(self, nums):
        pos, neg = [0] * len(nums), [0] * len(nums)
        pos[0], neg[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = max(nums[i], pos[i - 1] * nums[i])
                neg[i] = min(nums[i], neg[i - 1] * nums[i])
            else:
                pos[i] = max(nums[i], neg[i - 1] * nums[i])
                neg[i] = min(nums[i], pos[i - 1] * nums[i])
        return max(pos)

print(Solution().maxProduct([2, 3, -2, 4]))		# 6
print(Solution().maxProduct([-2, 0, -1]))		# 0
print(Solution().maxProduct([-2, 3, -4]))		# 24

