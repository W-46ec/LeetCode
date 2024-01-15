
"""
# Remove K Digits

Given string num representing a non-negative integer `num`, and an integer `k`, return *the smallest possible integer after removing `k` digits from `num`*.


**Example 1:** 
```
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

**Example 2:** 
```
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```

**Example 3:** 
```
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```

**Constraints:** 
    - `1 <= k <= num.length <= 10^5` 
    - `num` consists of only digits.
    - `num` does not have any leading zeros except for the zero itself.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:        
        # Let the lenght of num be N, the length of result will be N - k.
        # To make the result as small as possible, we want the significant 
        # bits of the result as smaller as possible.
        # Ideally, the digits in result are in increasing order.
        
        # Use a stack to maintain the order
        stack = []
        # Start from the most significant bit
        for x in num:
            # If the current digit < top of stack, it means we can pop
            # that larger digit out and replace it with the smaller
            # digit to obtain a overall smaller result.
            while k and stack and stack[-1] > x:
                stack.pop()
                k -= 1
            stack.append(x)
        
        # If k is still larger than 0, we simply just truncate the in 
        # the right as the small digits are as far left as possible.
        # Don't forget to remove the leading zeros.
        res = "".join(stack[ : len(stack) - k]).lstrip('0')
        return res if res else '0'

# "1219"
print(Solution().removeKdigits("1432219", 3))

# "200"
print(Solution().removeKdigits("10200", 1))

# "0"
print(Solution().removeKdigits("10", 2))

# "0"
print(Solution().removeKdigits("10", 1))

# "11"
print(Solution().removeKdigits("1173", 2))

