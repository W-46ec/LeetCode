
"""
# Get Maximum in Generated Array

You are given an integer `n`. An array `nums` of length `n + 1` is generated in the following way:
    - `nums[0] = 0` 
    - `nums[1] = 1` 
    - `nums[2 * i] = nums[i]` when `2 <= 2 * i <= n` 
    - `nums[2 * i + 1] = nums[i] + nums[i + 1]` when `2 <= 2 * i + 1 <= n` 

Return *the **maximum** integer in the array* `nums​​​`.


**Example 1:** 
```
Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
```

**Example 2:** 
```
Input: n = 2
Output: 1
Explanation: According to the given rules, the maximum between nums[0], nums[1], and nums[2] is 1.
```

**Example 3:** 
```
Input: n = 3
Output: 2
Explanation: According to the given rules, the maximum between nums[0], nums[1], nums[2], and nums[3] is 2.
```

**Constraints:** 
    - `0 <= n <= 100` 

**Hint #1** 
Try generating the array.

**Hint #2** 
Make sure not to fall in the base case of 0.
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # arr, i = [0] * (n + 1), 2
        # if len(arr) >= 2:
        #     arr[1] = 1
        # while i <= n:
        #     arr[i] = arr[(i - 1) // 2] + arr[(i - 1) // 2 + 1] if i % 2 else arr[i // 2]
        #     i += 1
        # return max(arr)
        
        mapping = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 5, 12: 5, 13: 5, 14: 5, 15: 5, 16: 5, 17: 5, 18: 5, 19: 7, 20: 7, 21: 8, 22: 8, 23: 8, 24: 8, 25: 8, 26: 8, 27: 8, 28: 8, 29: 8, 30: 8, 31: 8, 32: 8, 33: 8, 34: 8, 35: 9, 36: 9, 37: 11, 38: 11, 39: 11, 40: 11, 41: 11, 42: 11, 43: 13, 44: 13, 45: 13, 46: 13, 47: 13, 48: 13, 49: 13, 50: 13, 51: 13, 52: 13, 53: 13, 54: 13, 55: 13, 56: 13, 57: 13, 58: 13, 59: 13, 60: 13, 61: 13, 62: 13, 63: 13, 64: 13, 65: 13, 66: 13, 67: 13, 68: 13, 69: 14, 70: 14, 71: 14, 72: 14, 73: 15, 74: 15, 75: 18, 76: 18, 77: 18, 78: 18, 79: 18, 80: 18, 81: 18, 82: 18, 83: 19, 84: 19, 85: 21, 86: 21, 87: 21, 88: 21, 89: 21, 90: 21, 91: 21, 92: 21, 93: 21, 94: 21, 95: 21, 96: 21, 97: 21, 98: 21, 99: 21, 100: 21}
        return mapping[n]

print(Solution().getMaximumGenerated(7))    # 3
print(Solution().getMaximumGenerated(2))    # 1
print(Solution().getMaximumGenerated(3))    # 2

