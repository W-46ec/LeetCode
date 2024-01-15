
"""
# Destination City

You are given the array `paths`, where `paths[i] = [cityA_i, cityB_i]` means there exists a direct path going from `cityA_i` to `cityB_i`. *Return the destination city, that is, the city without any path outgoing to another city*.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


**Example 1:** 
```
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
```

**Example 2:** 
```
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
```

**Example 3:** 
```
Input: paths = [["A","Z"]]
Output: "Z"
```

**Constraints:** 
    - `1 <= paths.length <= 100` 
    - `paths[i].length == 2` 
    - `1 <= cityA_i.length, cityB_i.length <= 10` 
    - `cityA_i != cityB_i` 
    - All strings consist of lowercase and uppercase English letters and the space character.
"""

import unittest
from random import randint, choices, shuffle
from typing import List
from collections import defaultdict
from functools import reduce

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        Create a graph where graph["cityA"] is the list of cities 
        that "cityA" has a direct path to.

        By definition, the graph of paths must form a line without any loop.
        Therefore, among all the source cities (i.e., graph.keys()), there should 
        be exactly 1 city (i.e., the starting node) with in-degree equal to 0 while 
        the rest of them have in-degree equal to 1. And all nodes in graph.keys() 
        must have out-degree equal to 1.

        Similarly, among all the destination cities (i.e., graph.values()), there 
        should be exactly 1 city (i.e., the end node) with out-degree equal to 0 while 
        the rest of them have out-degree equal to 1. And all nodes in graph.values() 
        must have in-degree 1.

        Therefore, we can easily find the distination node by subtracting the set of
        source cities from the set of destination cities.

        Example:
        "A" --> "B"     "C" --> "D"
                "B" --> "C"     "D" --> "F"
        So the destination node is {"B", "C", "D", "F"} - {"A", "B", "C", "D"}, which is {"F"}
        """
        graph = defaultdict(list)
        for src, dst in paths:
            graph[src] += [dst]
        return list(set(reduce(lambda x, y: x + y, graph.values())) - set(graph.keys()))[0]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.destCity([['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]), "Sao Paulo")

    def testcase2(self):
        self.assertEqual(self.soln_obj.destCity([['B', 'C'], ['D', 'B'], ['C', 'A']]), "A")

    def testcase3(self):
        self.assertEqual(self.soln_obj.destCity([['A', 'Z']]), 'Z')

    def test_random(self):
        num_tests = 1000
        for _ in range(num_tests):
            # Lowercase and uppercase English letters and the space character
            charset = "".join([chr(x) for x in range(65, 91)]) + "".join([chr(x) for x in range(97, 123)]) + ' '

            # Generate random paths
            num_paths, paths = randint(1, 100), []
            src, dst = "".join(choices(charset, k = randint(1, 10))), ""
            seen = {src}
            for _ in range(num_paths):
                dst = "".join(choices(charset, k = randint(1, 10)))
                while dst in seen:
                    dst = "".join(choices(charset, k = randint(1, 10)))
                seen.add(dst)
                paths += [[src, dst]]
                src = dst
            shuffle(paths)
            
            self.assertEqual(self.soln_obj.destCity(paths), dst)


if __name__ == '__main__':
    unittest.main()
