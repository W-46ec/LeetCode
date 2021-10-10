
"""
# Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports `[from, to]`, reconstruct the itinerary in order. All of the tickets belong to a man who departs from `JFK`. Thus, the itinerary must begin with `JFK`.

**Note:** 
    1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
    2. All airports are represented by three capital letters (IATA code).
    3. You may assume all tickets form at least one valid itinerary.
    4. One must use all the tickets once and only once.

**Example 1:** 
```
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
```

**Example 2:** 
```
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
```
"""

# Reference: https://leetcode.com/problems/reconstruct-itinerary/discuss/709877/Python3-DFS-Solution

from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets)
        graph = {}
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]
        ans, stack = [], ["JFK"]
        while stack:
            node = stack[-1]
            if node in graph and len(graph[node]) > 0:
                stack.append(graph[node].pop(0))
            else:
                ans.append(stack.pop())
        return ans[::-1]


print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

