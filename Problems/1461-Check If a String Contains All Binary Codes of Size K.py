
"""
# Check If a String Contains All Binary Codes of Size K

Given a binary string `s` and an integer `k`.

Return *True* if every binary code of length `k` is a substring of `s`. Otherwise, return *False*.


**Example 1:** 
```
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
```

**Example 2:** 
```
Input: s = "00110", k = 2
Output: true
```

**Example 3:** 
```
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
```

**Example 4:** 
```
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
```

**Example 5:** 
```
Input: s = "0000000001011100", k = 4
Output: false
```

**Constraints:** 
    - `1 <= s.length <= 5 * 10^5` 
    - `s` consists of 0's and 1's only.
    - `1 <= k <= 20` 

**Hint #1** 
We need only to check all sub-strings of length k.

**Hint #2** 
The number of distinct sub-strings should be exactly 2^k.
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # # Time Limit Exceeded
        # return all([format(i, '0' + str(k) + 'b') in s for i in range(2 ** k)])

        # Reference: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solution/
        total, seen = 1 << k, set()
        for i in range(k, len(s) + 1):
            curr = s[i - k : i]
            if curr not in seen:
                seen.add(curr)
                total -= 1
                if total == 0:
                    return True
        return False

# True
print(Solution().hasAllCodes("00110110", 2))

# False
print(Solution().hasAllCodes("0000000001011100", 4))

# False
print(Solution().hasAllCodes("0110", 2))

# False
print(Solution().hasAllCodes("10100110111010100000011110001010001100111110110100101010000011110110011010100000100000111000000001000110011100001010010101100100110001111101010101011110111001001100001000000110101000101100010110000001110010101000100001101001010100011101010110000100010011001001111110100101101010110101101111110010110011010010001100110011110100011101100111011001111101010100100110101001101011111100101110101111100011110010100111100111001110110001000110010001110011110000110010111100000110001011011001101100101111101100010010111110111010111000101111101010000000010010101110110100110101100010100010111111101010000011001100101110100010011101010111110011101010101101011001101110110111001110110001111000110011010011110111000111111011101101110010110101101100110000111101111111000100101110000010000101001100011110011011111110101100110010110101001111010110110110101100001010111010110000110111110111101111111110", 16))

