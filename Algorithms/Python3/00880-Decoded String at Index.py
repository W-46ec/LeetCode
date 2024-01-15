
"""
# Decoded String at Index

You are given an encoded string `s`. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:
    - If the character read is a letter, that letter is written onto the tape.
    - If the character read is a digit `d`, the entire current tape is repeatedly written `d - 1` more times in total.

Given an integer `k`, return *the `kth` letter (**1-indexed**) in the decoded string*.


**Example 1:** 
```
Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
```

**Example 2:** 
```
Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
```

**Example 3:** 
```
Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".
```

**Constraints:** 
    - `2 <= s.length <= 100` 
    - `s` consists of lowercase English letters and digits `2` through `9`.
    - `s` starts with a letter.
    - `1 <= k <= 10^9` 
    - It is guaranteed that `k` is less than or equal to the length of the decoded string.
    - The decoded string is guaranteed to have less than `2^63` letters.
"""

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        The idea is similar to the integer division, except that the repeated parts for
        integer are always the powers of 10. And here the repeated parts are strings.
        """
        # We first calculate the total length of the decoded string
        length = 0
        for c in s:
            if c.isdigit():
                length *= int(c)
            else:
                length += 1
        
        # We start from the back of s (i.e., "least significant digit") and deal with 
        # the "remainder" first. 
        # If we see a digit, it means the string we currently have is the concatenation 
        # of some repeated substrings. In that case, we can simply reduce the size of the 
        # string (i.e., "do a division") and focus only on 1 copy of the substring.
        # If we see a letter, it means we are dealing with the "remainder". Check if
        # the size of the current string is equal to k. If yes, return the current letter.
        # Otherwise, keep reducing the size of string.
        for c in s[::-1]:
            if c.isdigit():
                length //= int(c)
                k %= length
            else:
                if k % length == 0:
                    return c
                length -= 1

# o
print(Solution().decodeAtIndex("leet2code3", 10))

# h
print(Solution().decodeAtIndex("ha22", 5))

# a
print(Solution().decodeAtIndex("a2345678999999999999999", 1))

# x
print(Solution().decodeAtIndex("cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg", 480551547))

# a
print(Solution().decodeAtIndex("a23", 6))
