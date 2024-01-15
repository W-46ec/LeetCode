
"""
# String to Integer (atoi)

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:
    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is `0`. Change the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `-2^31` should be clamped to `-2^31`, and integers greater than `2^31 - 1` should be clamped to `2^31 - 1`.
    6. Return the integer as the final result.

**Note:** 
    - Only the space character `' '` is considered a whitespace character.
    - **Do not ignore** any characters other than the leading whitespace or the rest of the string after the digits.

**Example 1:** 
```
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.
```

**Example 2:** 
```
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.
```

**Example 3:** 
```
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.
```

**Constraints:** 
    - `0 <= s.length <= 200` 
    - `s` consists of English letters (lower-case and upper-case), digits `(0-9)`, `' '`, `'+'`, `'-'`, and `'.'`.
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        ans, idx, sign = 0, 0, 1

        # Strip all white spaces and split the string by space
        for word in str.strip().split(' '):
            # Update the sign if the first char is '-'
            if len(word) and (word[idx] == '-' or word[idx] == '+'):
                sign = -1 if word[0] == '-' else 1
                idx += 1

            # Keep reading until we reach a non-digit character
            while idx < len(word) and word[idx].isdigit():
                ans = ans * 10 + int(word[idx])
                idx += 1

            # We only need to consider the first word
            break

        # Clamp the integer so that it remains in [-2^31, 2^31 - 1].
        return min(max(-2 ** 31, ans * sign), 2 ** 31 - 1)

print(Solution().myAtoi("42"))                  # 42
print(Solution().myAtoi("   -42"))              # -42
print(Solution().myAtoi("4193 with words"))     # 4193
print(Solution().myAtoi("words and 987"))       # 0
print(Solution().myAtoi("91283472332"))         # 2147483648
print(Solution().myAtoi("   -23 44"))           # -23
print(Solution().myAtoi("3.14159"))             # 3
print(Solution().myAtoi("+1"))                  # 1
print(Solution().myAtoi("+"))                   # 0
print(Solution().myAtoi("2147483648"))          # 2147483647
print(Solution().myAtoi("+-12"))                # 0
print(Solution().myAtoi(""))                    # 0
print(Solution().myAtoi("00000-42a1234"))       # 0
