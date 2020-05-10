
"""
# Find the Town Judge

In a town, there are `N` people labelled from `1` to `N`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
    1. The town judge trusts nobody.
    2. Everybody (except for the town judge) trusts the town judge.
    3. There is exactly one person that satisfies properties 1 and 2.

You are given `trust`, an array of pairs `trust[i] = [a, b]` representing that the person labelled `a` trusts the person labelled `b`.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return `-1`.


**Example 1:** 
```
Input: N = 2, trust = [[1,2]]
Output: 2
```

**Example 2:** 
```
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
```

**Example 3:** 
```
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

**Example 4:** 
```
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
```

**Example 5:** 
```
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
```

Note:
    1. `1 <= N <= 1000` 
    2. `trust.length <= 10000` 
    3. `trust[i]` are all different
    4. `trust[i][0] != trust[i][1]` 
    5. `1 <= trust[i][0], trust[i][1] <= N` 
"""

from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N <= 1:
            return 1
        lst = [x for x in range(1, N + 1)]
        d = {}
        for a, b in trust:
            lst[a - 1] = -1
            if b not in d:
                d[b] = set()
            d[b].add(a)
        for i in range(len(lst)):
            if lst[i] != -1:
                if lst[i] in d and len(d[lst[i]]) == N - 1:
                    return lst[i]
        return -1

print(Solution().findJudge(2, [[1, 2]]))                    # 2
print(Solution().findJudge(3, [[1, 3], [2, 3]]))            # 3
print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))    # -1
print(Solution().findJudge(1, []))                          # 1
