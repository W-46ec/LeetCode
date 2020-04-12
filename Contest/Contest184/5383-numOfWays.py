
"""
# Number of Ways to Paint N × 3 Grid

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).
You are given n the number of rows of the grid.
Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.


Example 1:
Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:
[e1.png]

Example 2:
Input: n = 2
Output: 54

Example 3:
Input: n = 3
Output: 246

Example 4:
Input: n = 7
Output: 106494

Example 5:
Input: n = 5000
Output: 30228214


Constraints:
    - n == grid.length
    - grid[i].length == 3
    - 1 <= n <= 5000
"""

class Solution:
    def numOfWays(self, n: int) -> int:
        three1, two1 = 6, 6
        for i in range(2, n + 1):
            three2 = 2 * three1 + 2 * two1
            two2 = 3 * two1 + 2 * three1
            three1, two1 = three2, two2
        return (three1 + two1) % (10 ** 9 + 7)

print(Solution().numOfWays(1))
print(Solution().numOfWays(2))
print(Solution().numOfWays(3))
print(Solution().numOfWays(7))
print(Solution().numOfWays(5000))
