
"""
# Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
    1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
    3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    5. An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
    1. The string size will be in the range [1, 100].
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        left, asterisk = [], []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                asterisk.append(i)
            else:
                if len(left) <= 0 and len(asterisk) <= 0:
                    return False
                if len(left):
                    left.pop(-1)
                else:
                    asterisk.pop(-1)
        # The remaining asterisks have to be turned into ')' or empty string
        while len(left) and len(asterisk):
            if len(asterisk) == 0:
                return False
            # Asterisks must come after the left parenthesis in order to cancel it out
            if left.pop(-1) > asterisk.pop(-1):
                return False
        return len(left) == 0

print(Solution().checkValidString("(*)"))               # True
print(Solution().checkValidString("(*"))                # True
print(Solution().checkValidString("(((*******))"))      # True
print(Solution().checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")) # False
