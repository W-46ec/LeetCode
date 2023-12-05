
"""
# Count of Matches in Tournament

You are given an integer `n`, the number of teams in a tournament that has strange rules:
    - If the current number of teams is **even**, each team gets paired with another team. A total of `n / 2` matches are played, and `n / 2` teams advance to the next round.
    - If the current number of teams is **odd**, one team randomly advances in the tournament, and the rest gets paired. A total of `(n - 1) / 2` matches are played, and `(n - 1) / 2 + 1` teams advance to the next round.

Return *the number of matches played in the tournament until a winner is decided*.


**Example 1:** 
```
Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.
```

**Example 2:** 
```
Input: n = 14
Output: 13
Explanation: Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.
```

**Constraints:** 
    - `1 <= n <= 200` 
"""

import unittest

class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            count += n // 2
            n -= n // 2
        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()
        self.answer = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29, 31: 30, 32: 31, 33: 32, 34: 33, 35: 34, 36: 35, 37: 36, 38: 37, 39: 38, 40: 39, 41: 40, 42: 41, 43: 42, 44: 43, 45: 44, 46: 45, 47: 46, 48: 47, 49: 48, 50: 49, 51: 50, 52: 51, 53: 52, 54: 53, 55: 54, 56: 55, 57: 56, 58: 57, 59: 58, 60: 59, 61: 60, 62: 61, 63: 62, 64: 63, 65: 64, 66: 65, 67: 66, 68: 67, 69: 68, 70: 69, 71: 70, 72: 71, 73: 72, 74: 73, 75: 74, 76: 75, 77: 76, 78: 77, 79: 78, 80: 79, 81: 80, 82: 81, 83: 82, 84: 83, 85: 84, 86: 85, 87: 86, 88: 87, 89: 88, 90: 89, 91: 90, 92: 91, 93: 92, 94: 93, 95: 94, 96: 95, 97: 96, 98: 97, 99: 98, 100: 99, 101: 100, 102: 101, 103: 102, 104: 103, 105: 104, 106: 105, 107: 106, 108: 107, 109: 108, 110: 109, 111: 110, 112: 111, 113: 112, 114: 113, 115: 114, 116: 115, 117: 116, 118: 117, 119: 118, 120: 119, 121: 120, 122: 121, 123: 122, 124: 123, 125: 124, 126: 125, 127: 126, 128: 127, 129: 128, 130: 129, 131: 130, 132: 131, 133: 132, 134: 133, 135: 134, 136: 135, 137: 136, 138: 137, 139: 138, 140: 139, 141: 140, 142: 141, 143: 142, 144: 143, 145: 144, 146: 145, 147: 146, 148: 147, 149: 148, 150: 149, 151: 150, 152: 151, 153: 152, 154: 153, 155: 154, 156: 155, 157: 156, 158: 157, 159: 158, 160: 159, 161: 160, 162: 161, 163: 162, 164: 163, 165: 164, 166: 165, 167: 166, 168: 167, 169: 168, 170: 169, 171: 170, 172: 171, 173: 172, 174: 173, 175: 174, 176: 175, 177: 176, 178: 177, 179: 178, 180: 179, 181: 180, 182: 181, 183: 182, 184: 183, 185: 184, 186: 185, 187: 186, 188: 187, 189: 188, 190: 189, 191: 190, 192: 191, 193: 192, 194: 193, 195: 194, 196: 195, 197: 196, 198: 197, 199: 198, 200: 199}

    def testcase1(self):
        for n in self.answer:
            self.assertEqual(self.soln_obj.numberOfMatches(n), self.answer[n])


if __name__ == '__main__':
    unittest.main()

