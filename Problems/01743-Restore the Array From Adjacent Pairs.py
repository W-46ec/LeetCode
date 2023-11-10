
"""
# Restore the Array From Adjacent Pairs

There is an integer array `nums` that consists of `n` **unique** elements, but you have forgotten it. However, you do remember every pair of adjacent elements in `nums`.

You are given a 2D integer array `adjacentPairs` of size `n - 1` where each `adjacentPairs[i] = [ui, vi]` indicates that the elements `ui` and `vi` are adjacent in `nums`.

It is guaranteed that every adjacent pair of elements `nums[i]` and `nums[i+1]` will exist in `adjacentPairs`, either as `[nums[i], nums[i+1]]` or `[nums[i+1], nums[i]]`. The pairs can appear **in any order**.

Return *the original array `nums`. If there are multiple solutions, return **any of them***.


**Example 1:** 
```
Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
```

**Example 2:** 
```
Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
```

**Example 3:** 
```
Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]
```

**Constraints:** 
    - `nums.length == n` 
    - `adjacentPairs.length == n - 1` 
    - `adjacentPairs[i].length == 2` 
    - `2 <= n <= 10^5` 
    - `-10^5 <= nums[i], ui, vi <= 10^5` 
    - There exists some `nums` that has `adjacentPairs` as its pairs.
"""

import unittest
from random import randint, sample, shuffle
from typing import List
from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Create an undirected graph
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u] += [v]
            graph[v] += [u]

        # Find the start node (could be the first or the last element in the array)
        start_node = [node for node in graph if len(graph[node]) == 1][0]

        # Run DFS to restore the array
        stack, visited, array = [start_node], { start_node }, []
        while stack:
            node = stack.pop()
            array += [node]
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return array


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        ans = [1, 2, 3, 4]
        self.assertEqual(self.soln_obj.restoreArray([[2, 1], [3, 4], [3, 2]]) in [ans, ans[::-1]], True)

    def testcase2(self):
        ans = [-2, 4, 1, -3]
        self.assertEqual(self.soln_obj.restoreArray([[4, -2], [1, 4], [-3, 1]]) in [ans, ans[::-1]], True)

    def testcase3(self):
        ans = [100000, -100000]
        self.assertEqual(self.soln_obj.restoreArray([[100000, -100000]]) in [ans, ans[::-1]], True)

    def testcase4(self):
        ans = [-10, 4, -3, 3, -1]
        self.assertEqual(self.soln_obj.restoreArray([[4, -10], [-1, 3], [4, -3], [-3, 3]]) in [ans, ans[::-1]], True)

    def test_random(self):
        num_tests = 10
        for _ in range(num_tests):
            n = randint(2, 10 ** 5)
            ans = sample(sample(range(-10 ** 5, 10 ** 5 + 1), k = n), k = n)
            adjacentPairs = sample([sample([ans[i], ans[i + 1]], k = 2) for i in range(n - 1)], k = n - 1)
            self.assertEqual(self.soln_obj.restoreArray(adjacentPairs) in [ans, ans[::-1]], True)


if __name__ == '__main__':
    unittest.main()
