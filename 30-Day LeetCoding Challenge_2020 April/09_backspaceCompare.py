
"""
# Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
    1. 1 <= S.length <= 200
    2. 1 <= T.length <= 200
    3. S and T only contain lowercase letters and '#' characters.

Follow up:
    - Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S1, S2 = [], []
        lst1, lst2 = list(S), list(T)
        idx = 0
        while idx < max(len(lst1), len(lst2)):
            if idx < len(lst1):
                if lst1[idx] == '#':
                    if len(S1) > 0:
                        S1.pop(-1)
                else:
                    S1.append(lst1[idx])
            if idx < len(lst2):
                if lst2[idx] == '#':
                    if len(S2) > 0:
                        S2.pop(-1)
                else:
                    S2.append(lst2[idx])
            idx += 1
        return "".join(S1) == "".join(S2)

print(Solution().backspaceCompare("ab#c", "ad#c"))
print(Solution().backspaceCompare("###", "#"))
