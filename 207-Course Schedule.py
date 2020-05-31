
"""
# Course Schedule

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]` 

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?


**Example 1:** 
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:** 
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

**Constraints:** 
    - The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about how a graph is represented.
    - You may assume that there are no duplicate edges in the input prerequisites.
    - `1 <= numCourses <= 10^5` 
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        graph = {}
        for c, p in prerequisites:
            if c in graph:
                graph[c].append(p)
            else:
                graph[c] = [p]

        for node in range(numCourses):
            stack, visited, visitedCount = [node], [False] * numCourses, 0
            if not visited[node]:
                while stack:
                    src = stack.pop(0)
                    if visitedCount != 0 and src == node:
                        return False
                    elif not visited[src]:
                        visited[src] = True
                        visitedCount += 1
                        stack += graph[src] if src in graph else []
        return True


print(Solution().canFinish(2, [[1, 0]]))                    # True
print(Solution().canFinish(2, [[1, 0], [0, 1]]))            # False
print(Solution().canFinish(3, [[0, 1], [0, 2], [1, 2]]))    # True
