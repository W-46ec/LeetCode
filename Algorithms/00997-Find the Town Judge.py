
"""
# Find the Town Judge

In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
    1. The town judge trusts nobody.
    2. Everybody (except for the town judge) trusts the town judge.
    3. There is exactly one person that satisfies properties 1 and 2.

You are given an array `trust` where `trust[i] = [a_i, b_i]` representing that the person labeled `a_i` trusts the person labeled `b_i`.

Return *the label of the town judge if the town judge exists and can be identified, or return `-1` otherwise*.


**Example 1:** 
```
Input: n = 2, trust = [[1,2]]
Output: 2
```

**Example 2:** 
```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

**Example 3:** 
```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

**Constraints:** 
    - `1 <= n <= 1000` 
    - `0 <= trust.length <= 10^4` 
    - `trust[i].length == 2` 
    - All the pairs of trust are **unique**.
    - `a_i != b_i` 
    - `1 <= a_i, b_i <= n` 
"""

from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # Special case: There's only one person -- the judge
        if N == 1:
            return 1
        
        # inbound_deg[k] -- The number of nodes that are pointing to k
        # outbound_deg[k] -- The number of nodes that k is pointing to
        inbound_deg = defaultdict(int)
        outbound_deg = defaultdict(int)
        
        # Find the in/outbound degree for each node
        for a, b in trust:
            inbound_deg[b] += 1
            outbound_deg[a] += 1
        
        # Find the node with inbound degree equal to N - 1
        # and outbound degree equal to 0
        for k in inbound_deg:
            if inbound_deg[k] == N - 1 and outbound_deg[k] == 0:
                return k
        return -1

# 2
print(Solution().findJudge(2, [[1, 2]]))

# 3
print(Solution().findJudge(3, [[1, 3], [2, 3]]))

# -1
print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))

# 1
print(Solution().findJudge(1, []))
