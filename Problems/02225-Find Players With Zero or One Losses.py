
"""
# Find Players With Zero or One Losses

You are given an integer array `matches` where `matches[i] = [winner_i, loser_i]` indicates that the player `winner_i` defeated player `loser_i` in a match.

Return *a list `answer` of size `2` where*:
    - `answer[0]` is a list of all players that have **not** lost any matches.
    - `answer[1]` is a list of all players that have lost exactly **one** match.

The values in the two lists should be returned in **increasing** order.

**Note:** 
    - You should only consider the players that have played **at least one** match.
    - The testcases will be generated such that **no** two matches will have the **same** outcome.


**Example 1:** 
```
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
```

**Example 2:** 
```
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
```

**Constraints:** 
    - `1 <= matches.length <= 10^5` 
    - `matches[i].length == 2` 
    - `1 <= winner_i, loser_i <= 10^5` 
    - `winner_i != loser_i` 
    - All `matches[i]` are **unique**.
"""

import unittest
from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Think of it as a directed graph, where each vertex represents a player.
        For any pair of vertices u, v, there is an edge from u to v
        if and only if player u defeated player v in a match.

        The problem can be solved by counting the in-degrees of each vertex.
        answer[0] is given by the list of all vertices with in-degree equal to 0.
        answer[1] is given by the list of all vertices with in-degree equal to 1.
        """
        in_degree = defaultdict(int)
        for x, y in matches:
            in_degree[x] += 0
            in_degree[y] += 1
        return [sorted([v for v in in_degree if in_degree[v] == 0]), sorted([v for v in in_degree if in_degree[v] == 1])]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]), [[1, 2, 10], [4, 5, 7, 8]])

    def testcase2(self):
        self.assertEqual(self.soln_obj.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]), [[1, 2, 5, 6], []])


if __name__ == '__main__':
    unittest.main()
