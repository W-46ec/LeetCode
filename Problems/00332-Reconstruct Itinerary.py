
"""
# Reconstruct Itinerary

You are given a list of airline `tickets` where `tickets[i] = [from_i, to_i]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.


**Example 1:** 
![332_itinerary1-graph](./img/332_itinerary1-graph.jpg)
```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

**Example 2:** 
![332_itinerary2-graph](./img/332_itinerary2-graph.jpg)
```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
```

**Constraints:** 
    - `1 <= tickets.length <= 300` 
    - `tickets[i].length == 2` 
    - `from_i.length == 3` 
    - `to_i.length == 3` 
    - `from_i` and `to_i` consist of uppercase English letters.
    - `from_i != to_i` 
"""

# Reference: https://leetcode.com/problems/reconstruct-itinerary/discuss/709877/Python3-DFS-Solution
# Reference: https://leetcode.com/problems/reconstruct-itinerary/solutions/4041944/95-76-dfs-recursive-iterative

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets):
            graph[src] += [dst]

        # # Recursive solution
        # itinerary = []
        # def dfs(src = "JFK"):
        #     while graph[src]:
        #         dfs(graph[src].pop(0))
        #     itinerary.append(src)
        # dfs()

        # Iterative solution
        itinerary, stack = [], ['JFK']
        while stack:
            src = stack[-1]
            if graph[src]:
                stack.append(graph[src].pop(0))
            else:
                itinerary.append(stack.pop())

        return itinerary[::-1]


# ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))

# ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

